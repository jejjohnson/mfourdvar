import typing as tp
import equinox as eqx
import diffrax as dfx
import functools as ft
import jax
import jax.numpy as jnp
from jaxtyping import PyTree, Array
from mfourdvar._src.utils import time_patches
from mfourdvar._src.priors.base import Prior

Solver = dfx.AbstractSolver
StepSize = dfx.AbstractAdaptiveStepSizeController
Adjoint = dfx.AbstractAdjoint


class DynamicalPrior(Prior):
    model: tp.Optional[PyTree]
    params: tp.Optional[PyTree]
    solver: Solver
    stepsize: StepSize
    adjoint: Adjoint

    def __init__(
        self,
        model: PyTree,
        params: tp.Optional[PyTree]=None,
        solver: Solver = dfx.Tsit5(),
        stepsize: StepSize = dfx.PIDController(rtol=1e-5, atol=1e-5),
        adjoint: Adjoint = dfx.RecursiveCheckpointAdjoint(),
    ):
        self.params = params
        self.model = model
        self.solver = solver
        self.stepsize = stepsize
        self.adjoint = adjoint

    def init_state(self, x: PyTree) -> PyTree:
        raise NotImplementedError()
        
    def __call__(self, x: PyTree) -> PyTree:
        raise NotImplementedError()


class DynIncrements(DynamicalPrior):
    
    def __call__(
        self,
        x: Array,
        ts: Array,
        dt: tp.Optional[float] = None,
        params: tp.Optional[PyTree] = None,
    ) -> PyTree:
        t0 = ts[0]
        t1 = ts[-1]

        # time step
        if dt is None:
            dt = ts[1] - ts[0]

        # initialize state
        state = self.model.init_state(x=x)

        saveat = dfx.SaveAt(ts=jnp.asarray([t1]))

        sol = dfx.diffeqsolve(
            terms=dfx.ODETerm(self.model),
            solver=self.solver,
            adjoint=self.adjoint,
            t0=t0,
            t1=t1,
            dt0=dt,
            y0=state,
            saveat=saveat,
            args=params if params is not None else self.params,
            stepsize_controller=self.stepsize,
        )

        return sol.ys
    
    def loss(
        self, 
        x: Array, 
        ts: Array, 
        x_gt: tp.Optional[Array] = None,
        params: tp.Optional[PyTree] = None,
    ) -> Array:
        """Dynamical Loss Function for Prior operator

        Eqn:
            R(u;θ) = || u - ϕ(u;θ)||

        Args:
            x (Array): an array of states, [timesteps, variables]
            ts (Array): an array of times, [timesteps, ]
            x_gt (Array): an array of true states, [timesteps, variables]

        Returns:
            loss (Array): a loss scalar value for the dynamical cost function
        """
        if x_gt is None:
            x_gt = x
        # create t batches
        ts = time_patches(ts)

        # check sizes
        msg = f"Size Mismatch: \n{x.shape} | {ts.shape} | {x_gt.shape}"
        assert len(x) - 1 == len(ts) == len(x_gt) - 1, msg
        
        fn = ft.partial(self, params=params)

        # dynamical one-step predictions
        x_pred = jax.vmap(fn, in_axes=(0, 0), out_axes=(0))(x[:-1], ts)

        # return an array
        x_pred = x_pred.array

        # mean squared error
        loss = jnp.sum((x_pred - x_gt[1:]) ** 2)
        return loss


class DynTrajectory(DynamicalPrior):
    def __call__(
        self,
        x: Array,
        ts: Array,
        dt: tp.Optional[float] = None,
        params: tp.Optional[PyTree] = None,
    ) -> PyTree:
        t0 = ts[0]
        t1 = ts[-1]

        # time step
        if dt is None:
            dt = ts[1] - ts[0]

        # initialize state
        state = self.model.init_state(x=x)
        
        saveat = dfx.SaveAt(ts=ts)
        

        sol = dfx.diffeqsolve(
            terms=dfx.ODETerm(self.model),
            solver=self.solver,
            t0=t0,
            t1=t1,
            dt0=dt,
            y0=state,
            saveat=saveat,
            args=params if params is not None else self.params,
            stepsize_controller=self.stepsize,
        )

        return sol.ys

    def loss(
        self, 
        x: Array, 
        ts: Array, 
        x_gt: tp.Optional[Array] = None,
        params: tp.Optional[PyTree] = None,
    ) -> Array:
        """Dynamical Loss Function for Prior operator

        Eqn:
            R(u;θ) = || u - ϕ(u;θ)||

        Args:
            x (Array): an array of states, [timesteps, variables]
            ts (Array): an array of times, [timesteps, ]
            x_gt (Array): an array of true states, [timesteps, variables]

        Returns:
            loss (Array): a loss scalar value for the dynamical cost function
        """
        if x_gt is None:
            x_gt = x

        # check sizes
        msg = f"Size Mismatch: \n{x.shape} | {ts.shape} | {x_gt.shape}"
        assert len(ts) == len(x_gt) == len(x_gt), msg

        # dynamical one-step predictions
        x_pred = self(x[0], ts[1:], params=params)

        # return an array
        x_pred = x_pred.array
        # print("here!")
        # print(x_pred.shape, x_pred[:-1].shape, x_gt[1:].shape)

        # mean squared error
        loss = jnp.sum((x_pred - x_gt[1:]) ** 2)
        return loss
