---
title: Space-Time Decomposition
subject: Modern 4DVar
short_title: Space & Time
authors:
  - name: J. Emmanuel Johnson
    affiliations:
      - CNRS
      - MEOM
    orcid: 0000-0002-6739-0053
    email: jemanjohnson34@gmail.com
license: CC-BY-4.0
keywords: data-assimilation, open-science
abbreviations:
---





> PDE Formulation/Inspiration

---
## Dynamical System


---
## Spatial Operators 

> Local & Global, Gradient & Integral, Numerical & ML


---
### Whirlwind Tour

#### Criteria

**Uniform Grid**. This determines if the grid structure is uniform or not.

**Mesh Invariant**. This determines if one can use arbitrary resolutions or not.

**Fixed Parameters**. The parameters of the transformation are fixed or not, e.g. convolutional kernel, kernel function hyper-parameters, neural network function parameters.

**Local vs Global**. This says if the transformation is a local transformation, e.g. gradient, or a global transformation, e.g. integral.

**Fixed Structure Transformation**. This is whether the transformation can be applied to any new arbitrary grid structure. This is especially useful for methods which


```{list-table} Hybrid Spatiotemporal Operators
:header-rows: 1
:name: space-time-operators

* - Class
  - Name
  - Uniform Grid
  - Mesh Invariant
  - Fixed Params
  - Local / Global
  - Fixed
* - Coordinate-Based
  - Kernels Methods
  - No
  - Yes
  - No
  - Both*
  - No
* - Coordinate-Based
  - Neural Fields
  - No
  - Yes
  - No
  - Both*
  - No
* - Numerical Operators
  - Finite Difference
  - No
  - No
  - No
  - Local
  - Yes
* - Numerical Operators
  - Finite Volume
  - No
  - No
  - No
  - Local
  - Yes
* - Numerical Operators
  - Finite Element
  - No
  - No
  - No
  - Local
  - Yes
* - Numerical Operators
  - Spectral Methods
  - No
  - No
  - No
  - Global
  - Yes
* - Neural Operators
  - Deep ONets [{cite}`10.1038/s42256-021-00302-5`]
  - No
  - Yes
  - No
  - Global
  - Yes
* - Neural Operators
  - FNO [{cite}`10.48550/arXiv.2108.08481`]
  - Yes
  - Yes
  - No
  - Global
  - Yes
```



---
## Time Steppers


> Integrals, Numerical & ML


**Fundamental Theorem of Calculus**
$$
u(x, t) = u_0 + \int_0^t F(u, u_0, \tau,)d\tau
$$
**Auto-Regressive**

$$
u(x, \Delta t) = u_0 + \int_0^{\Delta t} F(u, u_0, \Delta t,)d\tau
$$

**Criteria**
* Integral Approx - MC, IS, Quadrature, Taylor Expansion
* Implicit vs Explicit
* Fixed vs Variable Params
* Local (AR) vs Global (FC)
* Structured vs Unstructured - weird time steps

---
### Hybrid

$$
\partial_t u = 
\alpha \boldsymbol{F}_\text{dyn}(u, t;\boldsymbol{\theta}) + 
(1 - \alpha) \boldsymbol{F}_\text{param}(u, t;\boldsymbol{\theta})
$$

**Dynamical Model** - In this example, $\alpha=1$ and we assume that the system dynamics are **known** we can write our problem as a PDE.

**Surrogate Model** - In this case, $\alpha=0$ and we assume that the system dynamics are **unknown** and we cannot formulate our problem as a PDE.

**Hybrid Model** - In this case, $0 < \alpha < 1$ ad we assume that the system dynamics are **partially-known** and we can formulate portions of our problem (spatially, temporally, or both) as a PDE and the other portion as a parameterized function.


```{list-table} Hybrid Spatiotemporal Operators
:header-rows: 1
:name: space-time-operators

* - Name
  - Spatial
  - Temporal
  - Example
* - Numerical PDE
  - Finite Derivatives (Diff,Vol,Elem)
  - Time Stepper
  - QG + RK4 Scheme
* - Numerical PDE
  - Spectral Derivatives
  - Time Stepper
  - QG + RK4 Scheme
* - Surrogate
  - Spatial NN Operator
  - Temporal NN Operator
  - Neural Flows [{cite}`10.48550/arXiv.2110.13040`], PDE-Refiner [{cite}`10.48550/arXiv.2308.05732`], Message Passing PDE [{cite}`10.48550/arXiv.2202.03376`]
* - Surrogate
  - Spatiotemporal NN Operator
  - " "
  - [NerFs](https://neuralfields.cs.brown.edu/), ConvLSTM [{cite}`10.48550/arXiv.1506.04214`], FNO [{cite}`10.48550/arXiv.2108.08481`], CORAL [{cite}`10.48550/arXiv.2306.07266`]
* - Hybrid
  - Spatial NN Operator
  - TimeStepper
  - Neural ODE [{cite}`10.48550/arXiv.2202.02435`]
* - Hybrid
  - Finite Derivatives
  - Neural Network
  - PDE Solver [{cite}`10.48550/arXiv.2202.03376`]
* - Hybrid
  - Finite Der. + NN
  - TimeStepper
  - Universal Differential Equations [{cite}`10.48550/arXiv.2001.04385`]
* - Hybrid
  - Finite Der. + NN
  - TimeStepper + NN
  - FouRKS [{cite}`10.48550/arXiv.2304.07029`]
```
