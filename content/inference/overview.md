---
title: Inference
subject: Modern 4DVar
subtitle: How to think about modern 4DVar formulations
short_title: Overview
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

Traditionally, we like to think that we can estimate ... via the Empirical Risk Minimization (ERM) criteria given by

$$
z^* =
\underset{z}{\text{argmin}} \hspace{2mm}
\sum_{n=1}^N \boldsymbol{D}(z_n;\boldsymbol{\theta}) +
\boldsymbol{R}(z;\boldsymbol{\theta})
$$

where $D$ is a likelihood term (data fidelity) and $R$ is a prior term (regularization).
We know that solve predictors minimize the average KL-Divergence

$$
q^*(z|y) = 
\underset{q(z|y)}{\text{argmin}} \hspace{2mm}
\mathbb{E}_{z\sim p(z|y)}
\left[
D_{KL}\left[ p(z|y) || q(z|y) \right]
\right]
$$

This is an asymmetric measure of distance between two distributions.
We can expand this using the definition to be

$$
\begin{aligned}
D_{KL}\left[ p(z|y) || q(z|y) \right] &= 
\mathbb{E}_{z\sim q(z|y)}
\left[ 
  \log \frac{p(z|y)}{q(z|y)}
\right] \\
&= 
\mathbb{E}_{z\sim q(z|y)}
\left[ 
  \log p(z|y)
\right] + 
\mathbb{E}_{z\sim q(z|y)}
\left[ 
  -\log q(z|y)
\right]
\end{aligned}
$$







## Bayesian Learning Rule

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
