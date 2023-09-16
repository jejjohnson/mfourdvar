---
title: Bayesian Crash Course
subject: Modern 4DVar
subtitle: Bayesian Interpretation of all Problems
short_title: Bayes For Inference/Learning
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

> How do we formulate the prediction problem for our quantity of interest?


$$
\mathcal{F}: \text{Observations} \times \text{Parameters} \rightarrow \text{State}
$$

We have a decision about how we want to formulate this problem. 
There are two classes of methods: regression-based learning and objective-based learning

$$
\begin{aligned}
\text{Regression-Based}: && &&
\boldsymbol{\theta}^* &= 
\underset{\boldsymbol{u}}{\text{argmin}}\hspace{2mm}
\mathcal{L}(\boldsymbol{\theta}) \\
\text{Objective-Based}: && &&
\boldsymbol{u}^* &= 
\underset{\boldsymbol{u}}{\text{argmin}}\hspace{2mm}
\mathcal{J}(\boldsymbol{u},\boldsymbol{\theta})
\end{aligned}
$$


### Example: Sea Surface Height Interpolation


Recall the problem of the mapping problem we wish to solve

$$
\mathcal{F}: \eta_{obs} \times \boldsymbol{\Theta} \rightarrow \eta_{state}
$$


## Pros & Cons

**Regression-Based Losses**:
* **Pro:** If the objective, $\mathcal{J}(\boldsymbol{u},\boldsymbol{\theta})$, is computationally expensive, we don't need to compute this.
* **Pro:** Uses global information of $\boldsymbol{u}_{obs}$.
* **Pro:** Does not need to compute, $\boldsymbol{\nabla_u} \mathcal{J}(\boldsymbol{u},\boldsymbol{\theta})$
* **Con:** Do not have access to $\mathcal{J}(\boldsymbol{u},\boldsymbol{\theta})$
* **Con:** It may be expensive to compute $\boldsymbol{u}_{sim}$
* **Con:** May be hard when $\boldsymbol{u}^*(\boldsymbol{\theta})$ is not unique...

**Objective-Based Losses**:
* **Pro:** Uses objective information of $\boldsymbol{J}(\boldsymbol{u},\boldsymbol{\theta})$
* **Pro**: Faster, does not require $\boldsymbol{u}_{sim}$
* **Pro:** Easily learns non-unique $\boldsymbol{u}^*(\boldsymbol{\theta})$.
* **Con**: Can get stuck in local optima of $\mathcal{J}(\boldsymbol{u},\boldsymbol{\theta})$
* **Con**: Often requires computing $\boldsymbol{\nabla}_{\boldsymbol{u}}\mathcal{J}(\boldsymbol{u},\boldsymbol{\theta})$



## Examples

### Denoising

In this example, we are interested in denoising a set of observations, $\boldsymbol{y}_\text{obs}$. We are interesting in recovering the original signal which believe to be our state, $\boldsymbol{u}$. 
We assume that this can be denoised via a linear operator, $\mathbf{H}$. 
For simplicity, we assume iid Gaussian noise.

$$
\boldsymbol{y}_\text{obs} = \mathbf{H}\boldsymbol{u} + \varepsilon, 
\hspace{5mm} \varepsilon\sim\mathcal{N}(0,\sigma^2)
$$

We can write out the posterior using the Bayesian formulation.

$$
p(\boldsymbol{u}|\boldsymbol{y}_\text{obs}) \propto p(\boldsymbol{y}_\text{obs}|\boldsymbol{u})p(\boldsymbol{u})
$$

We are using linear operations and a Gaussian likelihood, we can use the conjugate posterior which would allow for simpler inference. 
We can write this as

$$
p(\boldsymbol{u}|\boldsymbol{y}_\text{obs}) \propto 
\exp\left( -\mathcal{J}\left(\boldsymbol{u},\boldsymbol{y}_\text{obs}\right) \right)
$$

which is connected to the Gibbs distribution. 
We are left with the objective function

$$
\mathcal{J}(\boldsymbol{u},\boldsymbol{y}_\text{obs}) = 
\frac{1}{2}||\boldsymbol{y}_\text{obs} - \mathbf{H}\boldsymbol{u}||^2_2 + 
\lambda||\boldsymbol{u}||_1
$$

* $\mathcal{J}$ - regularized reconstruction energy
* $\lambda$ - regularization coefficient


