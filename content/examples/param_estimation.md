---
title: Parameter Estimation
subject: Modern 4DVar
subtitle: What components can we use to learn the parameters?
short_title: Parameter Estimation
authors:
  - name: J. Emmanuel Johnson
    affiliations:
      - CNRS
      - MEOM
    orcid: 0000-0002-6739-0053
    email: jemanjohnson34@gmail.com
  - name: Feier Yan
    email: feyan@connect.ust.hk
  - name: Hugo Frezat
    email: hugo.frezat@gmail.com
license: CC-BY-4.0
keywords: data-assimilation, open-science
abbreviations:
    DA: Data Assimilation
    QG: Quasi-Geostrophic
    SWM: Shallow Water Model
---

> In this section, we will walk through the parameter estimation problem that usually occurs within geoscience problems. 

---

## Problem Setup

In the parameter estimation case, we are interested in estimating the parameter of a spatial operator.
This is a standard problem in machine learning whereby we are given a dataset, $\mathcal{D}$, and we are interesting in finding the best model, $\mathcal{M}$, that fits the data

$$
p(\mathcal{M}|\mathcal{D}) = 
\frac{p(\mathcal{D}|\mathcal{M})p(\mathcal{M})}
{p(\mathcal{D})}
$$

In the case of geosciences, we are often given an ordered, temporal sequence of observations.

$$
\mathcal{D} = \left\{ \boldsymbol{y}_t \right\}_{t=1}^T
$$

This sequence could be a:
* 1D time series of sea surface temperature values at a particular location
* 2D+T spatiotemporal time series of sea surface height within the gulfstream.

Our task is to find some parameterized model that is able to fit this sequence of observations

$$
\boldsymbol{y}_t = \boldsymbol{f}(t;\boldsymbol{\theta}) + \varepsilon_t, \hspace{5mm}
\varepsilon_t \sim \mathcal{N}(0,\sigma^2)
$$

---
### Dynamical System


For different purposes, we often want to find the best dynamical model that fit this sequence of observations.
Fortunately, the entire field of physics is governed by dynamical models where we can draw inspiration from. 
The typical formulation of a dynamical system which is a description of the spatial dynamics wrt the change in time. We can write it like so:

$$
\begin{aligned}
\text{Dynamical Model}: && &&
\boldsymbol{u}_t &= \boldsymbol{\Phi}\left(\boldsymbol{u}_0, t; \boldsymbol{\theta}\right)\\
\text{Observation Model}: && &&
\boldsymbol{y}_t &= \mathbf{H}\cdot\boldsymbol{u}_t + \varepsilon_t, \hspace{5mm}
\varepsilon_t \sim \mathcal{N}(0,\boldsymbol{\Sigma}_t)
\end{aligned}
$$ (eq:dynamical-system)

where $\boldsymbol{\Phi}$ is a parameterized `ODESolver` which takes an initial state, $\boldsymbol{u}_0$ and outputs the state, $\boldsymbol{u}$, at time, $t$.
$\boldsymbol{H}$ is now a parameterized function that transforms the state, $u_t$, to the observation, $y_t$.
The time domain, $\mathcal{T}$ is typically defined on the positive real number line.
For convenience, we often consider it to be bounded between $0$ and $T$, i.e., $\mathcal{T}=[0,T]$.


---

### Parameter Posterior 

We will rewrite the posterior given our formulation.

$$
p(\boldsymbol{\theta}|\mathcal{D}) = 
\frac{1}{Z}
p(\boldsymbol{y}|\boldsymbol{u},\boldsymbol{\theta})
p(\boldsymbol{\theta})
$$

where $Z$ is the evidence, $Z=\int p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta})d\boldsymbol{\theta}$.

Due to our definition of the Gaussian likelihood, we can use the conjugate posterior which would allow for simpler inference. 
We can write this as

$$
p(\boldsymbol{\theta}|\mathcal{D}) \propto 
\exp\left( -\mathcal{L}\left(\boldsymbol{\theta}\right) \right)
$$

which is connected to the Gibbs distribution. 


---

### Loss Function

We are left with the maximum likelihood loss function

$$
\boldsymbol{\theta}^* = \underset{\boldsymbol{\theta}}{\text{argmin}}
\hspace{2mm}
\mathcal{L}(\boldsymbol{\theta})
$$

where the loss function is equal to

$$
\begin{aligned}
\mathcal{L}(\boldsymbol{\theta}) = 
\frac{1}{2\sigma^2}\sum_{t=1}^T
||\boldsymbol{y}_t - \boldsymbol{H}\circ \boldsymbol{\Phi}\left(\boldsymbol{u}_0, t; \boldsymbol{\theta}\right)||^2_{2}
\end{aligned}
$$





---
## Dynamical Model 

The dynamical system shown in equation [](#eq:dynamical-system) is the corner stone of ODEs and PDEs.
It describes the spatiotemporal decomposition of a field.

$$
\begin{aligned}
\partial_t \boldsymbol{u}(t) &= \boldsymbol{F}\left(\boldsymbol{u}(t), t, \boldsymbol{\theta}\right),
\hspace{5mm}
\boldsymbol{u}(0) =\boldsymbol{u}_0, 
\hspace{5mm}
t \in [0, T]
\end{aligned}
$$ (eq:ode)

The spatial operator, $\boldsymbol{F}$, consists of the set of all possible combinations of linear operators and/or non-linear operators.
These are typically numerical like finite difference, finite volume, finite element or pseudospectral.
The solution to this can be written using the 2nd fundamental theorem of calculus


$$
\boldsymbol{\Phi}(\boldsymbol{u},\boldsymbol{\theta};t):=
\boldsymbol{u}(t) = \boldsymbol{u}(0) + 
\int_0^t\boldsymbol{F}\left(\boldsymbol{u}, \tau, \boldsymbol{\theta}\right)d\tau
$$ (eq:timestepper)

This equation involves evaluating an integral.
In practice, there are many ways to evaluate this integral numerically. 
For example, we could use Taylor expansion which is what Euler's method does or we could use a quadrature method which is what Runge-Kutta methods do. 
Regardless of the method chosen, most of the methods do not directly calculate the difference between $0$ and $T$ especially if the time horizon is very large. 
They typically fit them in an "autoregressive" way by incrementally applying the `timestepper` recursively from $0$ to $T$. 
So first, we define the increment operator for the solution to the dynamical system.

$$
\boldsymbol{\Phi}(\boldsymbol{u},\boldsymbol{\theta};t + \Delta t) := \boldsymbol{u}(t+\Delta t) = \boldsymbol{u}(t) + 
\int_t^{t+\Delta t}\boldsymbol{F}\left(\boldsymbol{u}, \tau, \boldsymbol{\theta}\right)d\tau
$$ (eq:timestepper-increment)

Now, we can apply it incrementally.

$$
\boldsymbol{\Phi}(\boldsymbol{u},\boldsymbol{\theta};t) =
\boldsymbol{\Phi}(\boldsymbol{u},\boldsymbol{\theta};T - \Delta t) 
\circ \boldsymbol{\Phi}(\boldsymbol{u},\boldsymbol{\theta};T - 2\Delta t) 
\circ \ldots
\circ \boldsymbol{\Phi}(\boldsymbol{u},\boldsymbol{\theta};\Delta t) 
\circ \boldsymbol{\Phi}(\boldsymbol{u},\boldsymbol{\theta};0) 
$$ (eq:timestepper-autoregressive)

where we arrive at equation [](#eq:timestepper)

For the purposes of discussing the parameter estimation problem, we don't need to focus on the underlying method of solving the ODE.
So for the remainder of this note, we will use the symbol $\boldsymbol{\Phi}(\boldsymbol{u},\boldsymbol{\theta})$ to denote the `odesolver` operator which takes the initial condition (or multiple initial conditions) and produces the solution, $\boldsymbol{u}$, to the ODE with the spatial operator $\boldsymbol{F}$ and the `timestepper` at the specified time steps, $t$.

---
### Pseudo-Code

<!-- :::{tip} Pseudo-Code - ODE Solver
:class: dropdown -->

Let's initialize all of the pieces that we are going to need from the ODE in equation [](#eq:ode).
First, we need to initialize the parameterized spatial operator, $\boldsymbol{F}$. 

```python
# initialize inputs
params: PyTree = ...
F: Callable = ...
```

For this section, we are not concerned with the particular form of the function, $\boldsymbol{F}$ because it is not important for this discussion. 
In the following sections, we will consider what form it will take.

Recall the equation for a single stepper as [](#eq:timestepper-increment).
We can write some pseudo-code to define our custom `TimeStepper` like so:

```python
# initialize integral solver, e.g. Euler, Runga-Kutta, Adam-Bashforth
integral_solver: Callable = ...

def time_stepper(u: Array, params: PyTree, t0: float, t1: float) -> Array:
  
    # calculate the increment (the integral)
    u_increment = integral_solver(F, u, params, t0, t1)

    # add increment to initial condition
    return u + u_increment
```

Here, we are only calculating the solution to the ODE between $t$ and $t +\Delta t$.
To calculate the recursive step to calculate the full solution to the ODE from equation [](#eq:timestepper), we can do it manually by defining a time vector, $\mathbf{t}$, with all of the time intervals where we want out output state, $\boldsymbol{u}_t$.

$$
\mathbf{t} = 
\left[t_0, t_{\Delta t}, t_{2\Delta t}, \ldots,  t_{T-2\Delta t}, t_{T-\Delta t}, t_{T}\right] \in \mathbb{R}^T
$$
We can also initialize our state, $\boldsymbol{u}_0$.

```python
# initialize state
u0: Array = ...
# initialize time steps
time_steps = jnp.arange(0, T, dt)
```

Now we can apply our `time_stepper` function recursively.

```python


u_solutions: List = []

# loop through list of time steps
for t in time_steps:
    # time step
    u: Array[""] = time_stepper(F, u, t, t+dt, params)
    # store the solutions
    u_solutions.append(u)

# concatenate the solutions
u_solutions: Array["T-1"] = jnp.stack(u_solutions, axis=0)
```

However, most modern functions have this functionality built into the software. 
So we only have to call it on the initial condition.

```python
# initialize time steps
dt = 0.01

# do everything in one shot.
u: Array["T-1"] = package.time_stepper(F, u0, params, t0=0, t1=T, dt=dt)
```

**Tip**: Sometimes there is advanced functionality to output the solution at a different time intervals than what we want to march at. 
For example, we may want to increment at a finer time step but we output at less frequency to match the observations.

```python
# initialize time steps
dt = 0.01

# time steps for saving the output vector
dt_saved = 0.1
saved_time_steps = jnp.arange(0, T, dt_saved)

# do everything in one shot.
u: Array["T-1"] = package.time_stepper(F, u0, params, t0=0, t1=T, dt=dt, saveas=saveas)
  ```

<!-- ::: -->

---
## Parameter Learning 

There are many cases where we believe we have a prior belief about the underlying dynamical system that would fit the observations. 
However, often times there can be unclear parameters within the dynamical model itself.
We can use the same learning scheme shown above to try and fit the best parameters, $\theta$, given the observations, $y$.

### Pseudo-Code


```python
# initialize pde rhs function, e.g. L63, L96, QG
pde_params: PyTree = ...
pde_rhs: Callable = ...

# initialize neural network model
nn_params: PyTree = ...
nn_model: Callable = ...

# concat params
params = (pde_params, nn_params)

# create NN function
def equation_of_motion(state: Array[""], params: PyTree) -> Array[""]:

	# unpack the parameters
	pde_params, nn_params = params

	# PDE equation of motion --> Update State
	new_state: Array[""] = pde_rhs(state, pde_params)

	# NN subgrid parameterization --> Correction
	correction: Array[""] = nn_model(state, nn_params)

	# update state with correction
	new_state: Array[""] += correction

	return new_state

# initialize state
y_sim: Array["T"] = ...

# where to save the array
t0, t1, dt = ...
saveas: Array["T-1"] = np.arange(t0, t1, dt)

# loop through epochs
for iepoch in num_epochs:

	# forward
	y_hat: Array["T-1"] = dfx.integrate(equation_of_motion, params, y_sim[0][""], t0, t1, dt, saveas)

	# compute loss
	loss_value: Array["T-1"] = loss_function(y_hat, y[1:])
	loss_value: Array[""] = mean(loss_value)

	# calculate gradients wrt params
	# update params with new gradients
	
```
	

---
### Example: Lorenz-96

We can write the dynamical model for the 2-Level Lorenz 96 equation.

$$
\begin{aligned}
\frac{dx}{dt} &= (x_{i+1} - x_{i-2})x_{i-1}-x_i + F - \frac{h c}{b} \sum_{j}y_j \\
\frac{dy}{dt} &= -b c (y_{j+2} - y_{j-1})y_{j+1}- c y_j  - \frac{h c}{b} x_i 
\end{aligned}
$$ (eq:lorenz96)

There are a few parameters within this formulation like $h$, $c$, and $b$.


---
### Example: **Quasi-Geostrophic Equation**

$$
\partial_t \omega + \boldsymbol{\nabla}\boldsymbol{u}\cdot\omega = 
\nu\boldsymbol{\nabla}^2\omega-
\beta\partial_x\psi -\mu\omega + F
$$

There are a few parameters within this formulation which include the Rossby parameter, $\beta$, the viscosity, $\nu$, and the linear drag coefficient, $\mu$.


**Pseudo-Code**

```python
params: PyTree = ...
forcing_fn: Callable = ...


def equation_of_motion(q, params):

    psi = elliptical_inversion(q, beta=params.rossby_radius, method="cg")

    u, v = geostrophic.velocities(psi)

    rhs_adv = advection_2D(q, u, v)

    rhs_beta = geostrophic.beta_plane(q, beta=params.beta)

    rhs_diffusion = diffusion_2D(q, viscosity=params.viscosity)

    forcing = forcing_fn(q)

    return - rhs_adv + rhs_beta + rhs_diffusion + forcing_fn
```




---
## Hybrid Models

First, we need to choose our parameterized spatial operator $\boldsymbol{F}$.

$$
\boldsymbol{F}(\boldsymbol{u},t;\boldsymbol{\theta}) = 
\alpha \boldsymbol{F}_\text{dyn}(u, t;\boldsymbol{\theta}) + 
(1 - \alpha) \boldsymbol{F}_\text{param}(u, t;\boldsymbol{\theta})
$$

From this formulation, we can consider three types of models that is found within the literature.

**Dynamical Model**. In this example, $\alpha=1$ and we have a strong assumption about the underlying dynamics that can fit the observations. 
We do not add any parameterizations.
This can be written as a classical dynamical model given as the solution to an ODE or PDE. 
In the case of PDEs, this can included a model like the QG model or SWM.

**Surrogate Model**. In this case, $\alpha=0$ and we assume that we have very weak assumptions about the underlying dynamics that can describe the observations. the system dynamics are **unknown** and we cannot formulate our problem as a PDE.

**Hybrid Model**. In this case, $0 < \alpha < 1$ ad we assume that the system dynamics are **partially-known** and we can formulate portions of our problem (spatially, temporally, or both) as a PDE and the other portion as a parameterized function.


**Note**: there is a blurred line between a pure dynamical model and a surrogate model. 
For example, a parameterized model can come in many forms (see table [](tb:model-architecture-whirlwind) for examples). 
One could argue that trying to find the parameters to a forcing function that follows a particular form, e.g. linear, periodic, or polynomial, could be considered learning a forcing function.

$$
\begin{aligned}
\end{aligned}
$$

This formulation is based on the paper [{cite}`10.48550/arXiv.2107.07687`]




---
### Spatial Parameterization

* Denoising, Calibration, Forcing Term
* 

---
### Subgrid Parameterization


```python
# define pde model
pde_model: Callable = ...
# define subgrid parameterization term
nn_model: Callable = ...

#
```

This example was inspired by [{cite}`10.1029/2022MS003124,10.1029/2022MS003258`].

---
### Surrogate Models


This is known as Neural ODE [{cite}`10.48550/arXiv.2202.02435,10.48550/arXiv.1806.07366`] within the literature.


---
## Offline Learning

In the above examples, we were using a fully differentiable model to learn the forcing for a dynamical model. 
So we could simply train the parameterizations on simulation data.
We call this *offline learning* because we are not running any dynamical models.
We are simply learning the parameterization with pairwise.
Naturally, since we call this offline, then all of the examples above underneath the **hybrid modeling** section would be considered *online learning* in some communities.

$$
\mathcal{D} = \left\{ \boldsymbol{y}_n,\boldsymbol{u}_n \right\}_{n=1}^N
$$

where $(u,y)$ comes from pairwise data points from a twin experiment.

$$
\boldsymbol{y}_n = \boldsymbol{f}(\boldsymbol{u}_n;\boldsymbol{\theta}) + \varepsilon_n, \hspace{5mm}
\varepsilon_t \sim \mathcal{N}(0,\boldsymbol{\Sigma}_t)
$$

---
### Example: Forcing Term

---
### Example: Subgrid Parameterization

---
### Example: Surrogate Models




---
## Model Uncertainty

We can take a completely probabilistic approach to this

$$
\begin{aligned}
\text{Initial State}: && &&
\boldsymbol{u}_0 &\sim p(\boldsymbol{u}_0;\boldsymbol{\theta}) \\
\text{Transition Dynamics}: && &&
\boldsymbol{u}_t &\sim p(\boldsymbol{u}_{t}|\boldsymbol{u}_{t-1};\boldsymbol{\theta}) \\
\text{Emission Dynamics}: && &&
\boldsymbol{y}_t &\sim p(\boldsymbol{y}_t|\boldsymbol{y}_{t-1};\boldsymbol{\theta}) \\
\end{aligned}
$$

There are parallels to some algorithms which are nonlinear extensions to the Kalman Filter, e.g., Extended Kalman Filter (EKF), Unscented Kalman Filter (UKF), and the Assumed Density Filter (ADF).
In addition, there are also parallels to the Ensemble Kalman Filter (EnsKF).

There are also connections to methods that try to learn a reduced order model (ROM), i.e., a transformation from the state space, $\boldsymbol{u}\in\mathbb{R}^{D_u}$, to a latent representation, $\boldsymbol{z}\in\mathbb{R}^{D_z}$, where $D_z << D_u$.
This has connections to Koopman theory [{cite}`10.48550/arXiv.2102.12086`] which postulates that there exists some non-linear transformation whereby the underlying dynamics are linear.
There are some methods which try to directly learn a linear reduced order space like Dynamic Mode Decomposition (DMD) [{cite}`10.3934/jcd.2014.1.391,10.1146/annurev-fluid-030121-015835`] or operator inference [{cite}`10.48550/arXiv.2102.00083`].
These linear approximations can easily be plugged into the Kalman Filter framework to account for some uncertainty.
There are similar methods in the machine learning community which directly try to learn the transformation via flow-like models, e.g., the Kalman variational autoencoder [{cite}`10.23919/FUSION49751.2022.9841369`] or the [normalizing Kalman Filter](https://proceedings.neurips.cc/paper/2020/hash/1f47cef5e38c952f94c5d61726027439-Abstract.html). The paper on dynamical variational autoencoders [{cite}`10.1561/2200000089`] is a great review on the family of methods available.
