---
title: Bayesian Learning Rule
subject: Modern 4DVar
subtitle: A generalization of many optimization schemes
short_title: Bayesian Learning Rule
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
    BLR: Bayesian Learning Rule
    VI: Variational Inference
    SGD: Stochastic Gradient Descent
    GD: Gradient Descent
---


We assume that there exists a subclass of distributions, $\mathcal{Q}$, which we can optimize over.
In this case, we will assume that $\mathcal{Q}$ is a regular set and minimal exponential family of the form

$$
q(z;\boldsymbol{\lambda}) = 
\boldsymbol{h}(\boldsymbol{z})
\exp 
\left[ 
  \left\langle \boldsymbol{\lambda}, \boldsymbol{T}(\boldsymbol{z})\right\rangle
  - \boldsymbol{A}(\boldsymbol{\lambda})
\right]
$$ (eq:exponential_family)

* $\boldsymbol{\lambda}\in\Omega\subset\mathbb{R}^M$ are the natural (or canonical) parameters. 
* $\boldsymbol{A}(\boldsymbol{\lambda})$ is the log partition (or cumulant) function which is finite, strictly convex and differentiable over $\Omega$.
* $\boldsymbol{T}(\boldsymbol{\lambda})$ is the sufficient statistics
$\langle \cdot,\cdot\rangle$ is an inner product
* $\boldsymbol{h}(\boldsymbol{\theta}$) is the base measure.


:::{note} Example: Multivariate Gaussian Distribution
:class: dropdown
An example of the exponential family is the multivariate Gaussian distribution.
Most of us know the form given as

$$
\mathcal{N}(\boldsymbol{z}|\mathbf{m},\mathbf{S}^{-1}) \propto 
\exp\left[ 
  -\frac{1}{2}(\boldsymbol{z} - \mathbf{m})^\top 
  \mathbf{P}(\boldsymbol{z} - \mathbf{m})
\right]
$$

we can also write this in the information form of the natural parameters given by

$$
\mathcal{N}(\boldsymbol{z}|\mathbf{m},\mathbf{S}^{-1}) \propto 
\exp\left[ 
  (\mathbf{Pm})^\top \boldsymbol{z} + 
  \text{Trace}\left(-\frac{\mathbf{P}}{2} \boldsymbol{zz}^\top\right)
\right]
$$

We can also write the expectation parameters [{cite}`10.48550/arXiv.2111.01732`]

$$
\begin{aligned}
\text{Moment Parameters}: &&
\boldsymbol{\theta} &= 
(\mathbf{m},\mathbf{P}) \\
\text{Natural Parameters}: &&
\boldsymbol{\lambda} &= 
(\mathbf{P}^{-1}\mathbf{m},-\frac{1}{2}\mathbf{P}^{-1}) \\
\text{Expectation Parameters}: &&
\boldsymbol{\mu} &= 
(\mathbf{m},\mathbf{mm}^\top+\mathbf{P}) \\
\end{aligned}
$$

:::

The expectation parameter is given by the following formula:

$$
\boldsymbol{\mu}(\boldsymbol{\lambda}) =
\mathbb{E}_{z\sim q(\boldsymbol{\lambda})}
\left[ 
  \boldsymbol{T}(\boldsymbol{z})
\right]
$$

This is a bijective function of $\lambda$.
Some examples include the multivariate normal distribution and the Bernoulli distribution.

The *Bayesian learning rule* (BLR) optimization algorithm tries to locate the best candidate $q^*(z;\lambda)$ in $\mathcal{Q}$ by updating the candidate $q(z;\lambda_k)$ with the natural parameter $\lambda_k$ at iteration $k$ using a sequence of learning rates $\rho_k>0$.
This equation is given by

$$
\lambda^{(k+1)} = \lambda^{(k)} - \rho_k\tilde{\nabla}_\lambda
\left[ 
  \mathbb{E}_{z\sim q(z;\lambda_k)}\left(p(z,y)\right)
  - \mathcal{H}(q(z;\lambda))
\right]
$$


<!-- $$
q^*(z|y) = 
\underset{q(z|y)}{\text{argmin}} \hspace{2mm}
\mathbb{E}_{}
\left[ p(y|z) \right] +
D_{KL}
\left[ q(z|y) || p(z|y)\right]
$$ -->
