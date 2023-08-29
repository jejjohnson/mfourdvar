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




---
## Examples

We have a few examples of how one can use the Shallow water equations to generate some simulations under different parameter regimes.

### Linear SWM

[![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)](./sw_linear_jet_api1)

In this example, we look at the linearized shallow water model given by:

$$
\begin{aligned}
\partial_t h &+ H
\left(\partial_x u + \partial_y v \right) = 0 \\
\partial_t u &- fv =
- g \partial_x h
- \kappa u \\
\partial_t v &+ fu =
- g \partial_y h
- \kappa v
\end{aligned}
$$ (eq:sw_linear)

We demonstrate how we can