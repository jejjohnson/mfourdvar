---
title: Physics Informed Loss Function
subject: Modern 4DVar
subtitle: How we can add physics into our models
short_title: Loss
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


# Model

The objective would be to somehow find the true functa. In geosciences, we can write some partial differential equations (PDE) that we believe describe how this field changes in space and time. In most cases, we typically denote this evolving field as $u$ which is some approximation to the true field $\boldsymbol{f}$.

$$
\boldsymbol{f}(\mathbf{x}_s,t)\approx\boldsymbol{u}(\mathbf{x}_s,t)\hspace{15mm}\boldsymbol{u}:\Omega\times\mathcal{T}\rightarrow\mathbb{R}^{D}
$$ (functa_field)

where field $u$ is a representation of the true field $f$. However, we need some way for this field, $u$, to be close to the true field $f$. So this is where the (partial) differential equations come into play. We state that this field needs to satisfy some constraints which we define as space-time operations. The associated PDE constraint is defined by some arbitrary differential operators on the field to describe how it changes in space and time. Therefore, the PDE can be thought of a set of equations that act as constraints to how the field needs to behave in space and time.  So we can add the PDE constraints as:

$$
\begin{aligned}
u &= \boldsymbol{u}(\mathbf{x}_s,t) \\
\text{s.t.  } \partial_tu &=\mathcal{N}[u;\boldsymbol{\theta}](\mathbf{x}_s,t)
\end{aligned}
$$ (functa_pde)

where $\mathcal{N}$ is the differential operator on the field and $\boldsymbol{\theta}$ are the (hyper-) parameters for the PDE. These parameters don’t actually exist in nature. They are artefacts introduced by the PDE which are often unknown and/or assumed based on some prior knowledge.

```{admonition} Example: Sea Surface Height
:class: dropdown idea
For our SSH variable, there are many approximate models we can use to describe the dynamics. One such model is the Quasi-Geostrophic equations given by

$$
\begin{aligned}
\eta &= \boldsymbol{\eta_\theta}(\mathbf{x}_s,t) && && &\boldsymbol{\eta_\theta}:\Omega\times\mathcal{T}\rightarrow\mathbb{R} \\
\text{s.t.   }\dot{\eta} &= -\frac{g}{f} \det\boldsymbol{J}(\eta,\nabla\eta)
\end{aligned}
$$

Through a series of assumptions, we approximate this. For this example, we know that this is a crude approximate of the actual dynamics. However, we can assume that this is “good enough”.

```



## Domain

Because our functa is often defined on a bounded domain, our PDE must also be able to understand the field on the bounded domain. For the spatial domain, we need to describe what happens at the edges (e.g. rectangle) of the domain. For the temporal domain, we need to describe what happens at the beginning of the domain, e.g. $t=0$. We can also define these as operators. Let’s define these as:

$$
\begin{aligned}
\mathcal{BC}[u;\boldsymbol{\theta}](\mathbf{x}_s,t) &=  \boldsymbol{u}_b, && &&
 \mathbf{x}_s\in\partial\Omega &&
 & &t\in\mathcal{T} \\
\mathcal{IC}[u; \boldsymbol{\theta}](\mathbf{x}_s,0) &= \boldsymbol{u}_0, && && \mathbf{x}_s\in\Omega
\end{aligned}
$$  (functa_pde_domain)

where $\mathcal{BC}$, are the boundary conditions on the field, $\mathcal{IC}$ are the initial conditions on the field. The boundary conditions dictate the behaviour on the spatial domain on the boundaries and the initial conditions dictate the behaviour at the initial condition, $t=0$. We find these a lot even in ML applications. For example, whenever we deal with convolutions on images, we need to think about what to do at the boundaries (the solution is almost always padding, a.k.a. ghost points). In toy problems in physics, we also often simplify these to make the problem easier and well-behaved. A common approach is to use periodic boundary conditions; which are very rare in nature; but they are very convenient because they allow us to use simpler solvers like spectral and pseudo-spectral solvers. If we have access to observations, then we can use these as initial and boundary conditions. This is often done in data assimilation fields like gap-filling and reanalysis.

---

# Parameterized Model

We could also assume that we don’t know anything about the physical equations that govern the system. However, we believe that we can learn about it from *data*. Let’s assume (by luck) we can define each pairwise spatial-temporal coordinate and field value of the *functa* that we are interested in. So we have a set of pairwise points which we can call a dataset $\mathcal{D}$ defined as

$$
\mathcal{D} = \left\{(\mathbf{x}_{s,n},t_n),\boldsymbol{f}_n \right\}_n^{\infty}
$$ (functa_model)

I say this is infinite because technically we can sample any continuous function infinitely many times without revisiting any previous samples (even on a bounded domain). The objective would be to find some sort of approximation of the actual function, $\boldsymbol{f}$, which maps each of these coordinate-values to the correct scaler/vector value. So we can define some arbitrary parameterized function, $\boldsymbol{f_\theta}$, which tries to approximate the functa. We can say that:

$$
\boldsymbol{f}(\mathbf{x}_s,t)\approx\boldsymbol{f_\theta}(\mathbf{x}_s,t)
$$

This parameters depend upon the architecture of the function we choose. Again, like the PDE, these parameters are artefacts introduced by the function. So for a linear function, we may have just a few set of parameters (weights and bias), for a basis function we may the same parameters with some additional hyper-parameters for the basis, and neural networks have many weights and biases which we apply compositionally. Now, if we have a flexible enough model and infinite data, we should be able to find such parameters to fit the functa. However, the problem becomes *how* to find those parameters. This is the *learning problem.* We assume the solution exists and we can find it. But the question becomes: 1) how do we find it and 2) how do we know we have found it. However, there is an entire field dedicated to trying to resolve these issues, e.g. optimization for finding the solution and defining the metrics for knowing if we’ve found it. In addition, I stated that we assume the problem exists and we have infinite data which is never true at all. So that only adds more problems…

## PINNS Formulation

**PDE Formulation**

* Equation of Motion
* Boundary Conditions
* Initial Conditions

Add governing equations to the loss function.

### Architectures

* MLP
* Random Fourier Features
* SIREN

### Training

This section was taken from [{cite}`10.48550/arXiv.2308.08468`]

---
### Example: Shallow Water Equations

This example was taken from [{cite}`10.1016/j.jcp.2022.111024`]

---
## Spatially Discretized

* CNN, Transformers, Neural Operators

### Example: Neural Operators

This example was taken from [{cite}`10.48550/arXiv.2111.03794`]

---
#### Example: Denoising

This example was taken from [{cite}`10.48550/arXiv.2210.16215`]

---
#### Example: Super Resolution

This example was taken from [{cite}`10.48550/arXiv.2306.10990`]


---
## Temporally Discretized

* LSTMs

---
## Spatiotemporally Discretized

* CNNs + LSTMs, Neural Operators
