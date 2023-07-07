---
title: Uncertainty Considerations
subject: Modern 4DVar
subtitle: How can we account for stochasticity
short_title: Uncertainty
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


$$
p(z|u,y,\theta) \propto p(y|z,\theta)p(u|z,\theta)p(z|\theta)p(\theta)
$$



## Stochastic Prior

We can assume that the QOI is jointly distributed with some hidden state, $\boldsymbol{z}$. So we can write the Bayesian formulation like so.

$$
p(\boldsymbol{u},\boldsymbol{z}) \propto
p(\boldsymbol{u}|\boldsymbol{z})p(\boldsymbol{z})
$$

We can say that the latent variable, $\boldsymbol{z}$, can be described by a (parameterized) prior distribution, $p(\boldsymbol{z};\boldsymbol{\theta})$. We also say that there exists some transformation, $\boldsymbol{T}(\cdot;\boldsymbol{\theta})$, which transforms the latent variable to the QOI.

$$
\boldsymbol{u} = 
\boldsymbol{T}(\boldsymbol{u}|\boldsymbol{z};\boldsymbol{\theta})
$$

The form of this transformation, $\boldsymbol{T}$, is the crux of many generative modeling papers. For example:

1. we can restrict the transformation to be bijective results in a [Normalizing flow model](https://lilianweng.github.io/posts/2018-10-13-flow-models/)
2. we can allow the transformation to be stochastic which results in a [Variational AutoEncoder (VAE) model](https://lilianweng.github.io/posts/2018-08-12-vae/) and stacking hierarchical stochastic transformations with some very specific design decisions results in a [diffusion model](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) which is a special case of a [hierarchical VAE](https://angusturner.github.io/generative_models/2021/06/29/diffusion-probabilistic-models-I.html).
4. Restricting the transformation to be surjective results in [SurVae Flows](https://arxiv.org/abs/2007.02731).

On a more practical note, this means that we can sample a latent variable from the prior distribution, and then propagate this sample through the conditional distribution to achieve a sample of our QOI.

$$
\begin{aligned}
\text{Prior}: && 
\boldsymbol{z} &\sim p(\boldsymbol{z};\boldsymbol{\theta})\\
\text{Conditional}: && 
\boldsymbol{u} &\sim 
p(\boldsymbol{u}|\boldsymbol{z};\boldsymbol{\theta}) \\
\end{aligned}
$$
 

## Stochastic Likelihood

$$
\begin{aligned}
\boldsymbol{z} &\sim p(\boldsymbol{z};\boldsymbol{\theta})\\
\boldsymbol{y} &\sim p(\boldsymbol{y}|\boldsymbol{z};\boldsymbol{\theta}) \\
\end{aligned}
$$


## Optimization Criteria

Let's define the minimization problem we are interested in:

$$
\boldsymbol{z}^* = \underset{\boldsymbol{z}}{\text{argmin}} \hspace{2mm}
\boldsymbol{J}(\boldsymbol{z};\boldsymbol{\theta})
$$

To find the optimal solution of this problem, we can write it down as:

$$
\boldsymbol{z}^{(k+1)} = \boldsymbol{z}^{(k)} + \boldsymbol{g}_k
$$

where $\boldsymbol{g}_k$ is some result of a generalized gradient operator

$$
[\boldsymbol{g}_k, \boldsymbol{h}_{k+1}] = \boldsymbol{g}(\boldsymbol{\nabla_z}\boldsymbol{J},\boldsymbol{h}_k, k; \boldsymbol{\phi})
$$

where $k$ is the iteration, $\boldsymbol{\phi}$ are the parameters of the gradient operator, and $\boldsymbol{h}$ is the hidden state.


**Note**: This is similar to the `JAX` API using optax

```python    
# apply gradients
params, opt_state = opt.apply_gradients()
```

There are ways to add stochasticity into this



