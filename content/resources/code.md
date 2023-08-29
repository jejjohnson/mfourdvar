---
title: Code
subject: Modern 4DVar
subtitle: Code-Bases to Help you Get started
short_title: Code
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
    GP: Gaussian Process
---


Below are some code bases that might be useful for people to get started.

---
## Algorithms

### Differentiable Ocean Models

**[jaxsw]()**. 
This library tries to . It uses components from other libraries like [equinox]() for PyTrees, [FiniteDiffX]() for finite differences, [kernex]() for interpretable convolution operators, and [diffrax]() for time steppers.

**[veros]()**.
This library is a fully-fledged Ocean GCM.


### 4DVarNet

This is a set of code bases that were used to design an end-to-end learning system for SSH interpolation.

[**4DVarNet-Core**]() [PyTorch]


[**4DVarNet-Starter**]() [PyTorch]


---
## Core Components

### PDE Elements

**[FiniteDiffX]()** - Finite Differences with JAX.

**[kernex]()** - stencil operations with JAX.

**[diffrax]()** - ODE time steppers with JAX.


---
### Optimization


**[JaxOpt](https://jaxopt.github.io/stable/)** - argmin differentiation with JAX.

**[Lineax](https://docs.kidger.site/lineax/)** - linear solvers with JAX.

**[TorchOpt](https://torchopt.readthedocs.io/en/latest/)**


### Simple Ocean Models

* pyQG - {cite}`10.5281/zenodo.6563667`
* jax-cfd - {cite}`10.1073/pnas.2101784118,10.48550/ARXIV.2207.00556`

**GCMs**

* veros - {cite}`10.5194/gmd-11-3299-2018`
* Oceananigans - {cite}`10.21105/joss.02018`



### Data Assimilation

* NCAR DART - {cite}`10.5065/D6WQ0202,10.1175/2009BAMS2618.1`
* https://www.jcsda.org/jcsda-project-jedi
* https://dj4earth.github.io/
* http://soca.jcsda.org/master/obs/