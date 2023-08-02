---
title: Shallow Water Model
subject: Differentiable Ocean Models
# subtitle: How can I estimate the state AND the parameters?
short_title: Shallow Water
authors:
  - name: J. Emmanuel Johnson
    affiliations:
      - CNRS
      - MEOM
    orcid: 0000-0002-6739-0053
    email: jemanjohnson34@gmail.com
license: CC-BY-4.0
keywords: jax, shallow water model, differentiable
abbreviations:
    SW: Shallow Water
    QG: Quasi-Geostrophic
    PDE: Partial Differential Equation
    RHS: Right Hand Side
    PV: Potential Vorticity
    SF: Stream Function
    N-S: Navier-Stokes
---


## Shallow Water


```{figure} https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjtdkiXdNKeWhSEVqnOImCqztCJKzySLLZNA&usqp=CAU
:name: fig-sw
:alt: Shallow Water Equations PDE.
:align: center

The shallow water equations schematic as per [{cite}`10.1017/9781107588431`].
```




$$
h(x,y,t) = \eta(x,y,t) - \eta_B(x,y,t)
$$

where $h$ is the total fluid thickness, $\eta$ is the height of the upper free surface, and $\eta_B$ is the height of the lower surface or the bottom topography.

For a single-layer fluid, and including the Coriolis term, the inviscid SW equations are defined as 

$$
\begin{aligned}
\text{Momentum}: && &&
D_t\vec{\boldsymbol{u}} + f\times \vec{\boldsymbol{u}} &= 
- g \boldsymbol{\nabla}\eta \\
\text{Mass}: && &&
\partial_t h + 
\boldsymbol{\nabla}\cdot(h\vec{\boldsymbol{u}}) &= 
0 
\end{aligned}
$$ (eq:sw_momentum_mass)

where $h\vec{\boldsymbol{u}}$ is the horizontal velocity.
We can expand these equations to be:

$$
\begin{aligned}
\text{Height}: && &&
\partial_t h + 
\partial_x (hu) + \partial_y (hv) &= 0\\
\text{Zonal Velocity}: && &&
\partial_t u + 
u \partial_x u + v\partial_y u - fv &=
- g \partial_x \eta \\
\text{Meridonal Velocity}: && &&
\partial_t v + 
u \partial_x v + v\partial_y v + fu &=
- g \partial_y \eta
\end{aligned}
$$  (eq:sw_nonlinear)

---

## Vector Invariant Formulation

We can rewrite the formulation for the momentum parts, $(u,v)$, in equation [](#eq:sw_nonlinear) in the vectorized notation

$$
\partial_t  \vec{\boldsymbol{u}} +
\vec{\boldsymbol{u}} \cdot \boldsymbol{\nabla} \vec{\boldsymbol{u}}
+ f\times \vec{\boldsymbol{u}} =
- g \boldsymbol{\nabla}h
$$ (eq:sw_nonlinear_vector)

We will use the vector identity of equation [](#eq:vector_identity) and plug this into equation [](#eq:sw_nonlinear_vector) to arrive at the vector form.

$$
\begin{aligned}
\text{Height}: && &&
\partial_t h &=  
-\partial_x (hu) - \partial_y (hv) = 0\\
\text{Zonal Velocity}: && &&
\partial_t u &= 
qhv
- g \eta - \partial_x (u^2 + v^2) \\
\text{Meridonal Velocity}: && &&
\partial_t v
&= - qhu
- g \partial_y\eta - \partial_y (u^2 + v^2)
\end{aligned}
$$  (eq:sw_nonlinear_vorticity)

where $q$ is the potential vorticity and $\frac{1}{2}(u^2+v^2)$ is the kinetic energy (equation [](#eq:kinetic_energy)).

:::{note} Proof
:class: dropdown

We will walk through the entire derivation.
Let's rewrite all of the terms

$$
\partial_t  \vec{\boldsymbol{u}} +
\vec{\boldsymbol{u}} \cdot \boldsymbol{\nabla} \vec{\boldsymbol{u}}
+ f\times \vec{\boldsymbol{u}} =
- g \boldsymbol{\nabla}h
$$ (eq:sw_nonlinear_vector)

We will use the vector identity in equation [](#eq:vector_identity) and plug this into equation [](#eq:sw_nonlinear_vector)

$$
\partial_t  \vec{\boldsymbol{u}} +
(\boldsymbol{\nabla}\times \vec{\boldsymbol{u}})\times
\vec{\boldsymbol{u}} +
\frac{1}{2}\boldsymbol{\nabla}(\vec{\boldsymbol{u}} \cdot \vec{\boldsymbol{u}})
+ f\times \vec{\boldsymbol{u}} =
- g \boldsymbol{\nabla}h
$$


We will rearrange the equation to isolate the curl portions

$$
\partial_t  \vec{\boldsymbol{u}} +
(\boldsymbol{\nabla}\times \vec{\boldsymbol{u}})\times
\vec{\boldsymbol{u}} +
f\times \vec{\boldsymbol{u}} =
- g \boldsymbol{\nabla}h -
\frac{1}{2}\boldsymbol{\nabla}(\vec{\boldsymbol{u}} \cdot \vec{\boldsymbol{u}})
$$

Now, we will collapse all like terms

$$
\partial_t  \vec{\boldsymbol{u}} +
(\boldsymbol{\nabla}\times \vec{\boldsymbol{u}} + f)\times \vec{\boldsymbol{u}} =
- g \boldsymbol{\nabla} \left(h +
\frac{1}{2}\vec{\boldsymbol{u}} \cdot \vec{\boldsymbol{u}}\right)
$$

We will use the definition of relative vorticity, $\zeta$ (equation [](eq:relative_vorticity)) and plug this into our equation

$$
\partial_t  \vec{\boldsymbol{u}} +
(\zeta + f)\times \vec{\boldsymbol{u}} =
- g \boldsymbol{\nabla} \left(h +
\frac{1}{2}\vec{\boldsymbol{u}} \cdot \vec{\boldsymbol{u}}\right)
$$

Now, we will use the definition of potential vorticity in the context of the height (equation [](#eq:potential_vorticity)) and plug this into our function.
With a sleight of hand, we will introduce a constant $\frac{h}{h}$ to make sure it works

$$
\partial_t  \vec{\boldsymbol{u}} +
q\times \vec{\boldsymbol{u}} =
- g \boldsymbol{\nabla} \left(h +
\frac{1}{2}\vec{\boldsymbol{u}} \cdot \vec{\boldsymbol{u}}\right)
$$

Now, we can expand the curl term to be

$$
\partial_t  \vec{\boldsymbol{u}} +
qh\vec{\boldsymbol{u}} =
- g \boldsymbol{\nabla} \left(h +
\frac{1}{2}\vec{\boldsymbol{u}} \cdot \vec{\boldsymbol{u}}\right)
$$

So we can rewrite the full formulas as

$$
\begin{aligned}
\text{Height}: && &&
\partial_t h &=  
-\partial_x (hu) - \partial_y (hv) = 0\\
\text{Zonal Velocity}: && &&
\partial_t u &= 
qhv
- g \eta - \partial_x (u^2 + v^2) \\
\text{Meridonal Velocity}: && &&
\partial_t v
&= - qhu
- g \partial_y\eta - \partial_y (u^2 + v^2)
\end{aligned}
$$  (eq:sw_nonlinear_vorticity)

where $q$ is the potential vorticity and $KE$ is the kinetic energy (equation [](#eq:kinetic_energy))

:::


---

## Linearized Shallow Water Equations

We can remove the advection terms from equation [](#eq:sw_nonlinear) by *linearizing* the PDE.

$$
\begin{aligned}
\frac{\partial h}{\partial t} &+ H
\left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} \right) = 0 \\
\frac{\partial u}{\partial t} &- fv =
- g \frac{\partial h}{\partial x}
- \kappa u \\
\frac{\partial v}{\partial t} &+ fu =
- g \frac{\partial h}{\partial y}
- \kappa v
\end{aligned}
$$ (eq:sw_linear)

This is appropriate for when the Rossby number is small. 
We also assume that the wave height is much smaller than the actual mean height. 

### Example Applications

#### Data Assimilation

This has been used in data assimilation schemes [{cite}`10.1029/2021ms002613`] to jointly assimilate observations of SSH whereby the a QG model was used for the balanced motions and a linear SW mode was used for the internal tides.



---
## HelpFul Tools

### Material Derivative

This is an operator that models the movement of a fluid parcel within a Eulerian framework.

$$
D_t = \partial_t + 
\vec{\boldsymbol{u}} \cdot \boldsymbol{\nabla} =
\partial_t + u\partial_x + v\partial_y
$$ (eq:material_derivative)


### Planetary Vorticity

$$
f(y) = 2\Omega\sin(\theta) + \frac{1}{R}2\Omega\cos(\theta) y
$$ (eq:planetary_vorticity)

where $f_0=2\Omega\sin(\theta_0)$ is the Coriolis force and $\beta=\frac{1}{R}2\Omega\cos(\theta_0)$ is the approximate $\beta$-plane forcing.
For more information, see this [wiki](https://en.wikipedia.org/wiki/Beta_plane) article for a better overview or this [video](https://www.youtube.com/watch?app=desktop&v=Ddj1CQdwOHY) for a more in-depth overview.


### Relative Vorticity

$$
\zeta = 
\partial_x v - \partial_y u = 
\boldsymbol{\nabla}\times\vec{\boldsymbol{u}}
$$ (eq:relative_vorticity)


### Potential Vorticity

$$
q = \frac{\zeta + f}{h}
$$ (eq:sw_potential_vorticity)

where $\zeta$ is the relative vorticity given by [](#eq:relative_vorticity), $f$ is the planetary vorticity given by [](#eq:planetary_vorticity).
A good overview between the relationshop between each of the vorticity equations can be found in this [youtube video](https://www.youtube.com/watch?v=6hmJ_3Es8xI).

### Kinetic Energy

$$
KE = \frac{1}{2}\left( u^2 + v^2\right)
$$ (eq:kinetic_energy)

### Vector Identity

$$
\vec{\boldsymbol{u}} \cdot \boldsymbol{\nabla}\vec{\boldsymbol{u}} =
(\boldsymbol{\nabla}\times \vec{\boldsymbol{u}})\times
\vec{\boldsymbol{u}} +
\frac{1}{2}\boldsymbol{\nabla}(\vec{\boldsymbol{u}} \cdot \vec{\boldsymbol{u}})
$$ (eq:vector_identity)