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