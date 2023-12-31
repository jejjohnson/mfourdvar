import typing as tp
import jax.numpy as jnp
import equinox as eqx
from jaxtyping import Array, PyTree
from mfourdvar._src.varcost.base import VariationalCost

WeakVarCost = VariationalCost


class StrongVarCost(VariationalCost):
    def loss(
        self,
        x,
        ts,
        y,
        mask: tp.Optional[Array] = None,
        xb: tp.Optional[Array] = None,
        params: tp.Optional[PyTree] = None,
        return_loss: bool = False,
    ):
        if xb is None:
            xb = x[0]

        # prior loss
        x = self.prior(x, ts)

        x = x.array

        # observation loss
        obs_loss = self.obs_op.loss(x, y, mask, params=params)

        # background loss
        background_loss = jnp.sum((x[0] - xb) ** 2)

        # compute variational loss
        var_loss = self.obs_op_weight * obs_loss
        var_loss += self.background_weight * background_loss

        # save other costs for auxillary outputs
        if return_loss:
            return var_loss, dict(var_loss=var_loss, obs=obs_loss, bg=background_loss)
        else:
            return var_loss
