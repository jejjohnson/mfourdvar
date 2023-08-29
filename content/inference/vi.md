---
title: Variational Inference
subject: Modern 4DVar
subtitle: How to think about modern 4DVar formulations
short_title: Variational Inference
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
    MAP: Maximum A Posteriori
    MLE: Maximum Likelihood Estimation
---

In this section, we will look at how we can infer the latent variables by exploiting the observed variables.
We are assuming that we cannot directly measure the latent variable and instead we can only measure the observations.
Following the notation throughout this book, the latent variables are $\boldsymbol{z}$ and the observed variables are $\boldsymbol{y}$.

Our goal is to perform inference, i.e. we are interested in estimating some hidden state given some observations.
We can define the posterior using Bayes rule

$$
p(\boldsymbol{z}|\boldsymbol{y}) =
\frac{p(\boldsymbol{z},\boldsymbol{y})}{p(\boldsymbol{y})}
$$ (eq:bayes_posterior)

where the numerator is the joint distribution for the latent variable and the observation and the denominator is the marginal likelihood or evidence for the observations.
The joint distribution can be easy to estimate because we can generally factor this quantity using conditional distributions, i.e.

$$
p(z,y)=p(y|z)p(z)
$$ (eq:bayes_posterior_factored)

However the marginal lieklihood needs to be calculated by integrating out the latent variables.

$$
p(y) = \int p(z,y)dz
$$ (eq:bayes_evidence)

This integral is generally intractable because it would mean integrating out all possible latent variables which we don't have access to. 
So we need to use alternative methods to try and estimate the posterior.

We can introduce a variational distribution from a family of possible distributions $\mathcal{Q}$ whereby we pick the best candidate $q^*(z)\in\mathcal{Q}$ that fits the true posterior $p(z|x)$.
In general, we want a distribution that is easy to calculate, e.g. Gaussian, Bernoulli, etc, so that we can exploit conjugacy for calculating quantities within the loss function. 
We could also employ a parameterized variational distribution which we would need to find given the observations, i.e. $q(z;\boldsymbol{\phi})$.

To measure the similarity between our approximate posterior and the true posterior, we will use an asymmetric distance metric called the Kullback-Leibler (KL) divergence.
This is given by

$$
D_{KL}\left[ q(z) || p(z|y)\right] =
\mathbb{E}_{z\sim q(z)} 
\left[ \log \frac{q(z)}{p(z|x)} \right] =
\mathbb{E}_{z\sim q(z)} 
\left[ - \log \frac{p(z|x)}{q(z)} \right]
$$

In our case, we would like to find the best candidate distribution $q^*$ st it minimizes the KL divergence

$$
q^*(z) = \underset{q}{\text{argmin}} \hspace{2mm}
D_{KL}\left[ q(z) || p(z|y)\right]
$$

In the above equation, we don't have access to the true posterior so we will use the Bayes rules for the posterior [](#eq:bayes_posterior) that we outlined earlier.
We can plug the RHS of this equation into our KLD minimization problem to get

$$
D_{KL}\left[ q(z) || p(z|y)\right] =
\mathbb{E}_{z\sim q(z)} 
\left[ - \log p(\boldsymbol{z},\boldsymbol{y}) + \log q(z) \right] +
\log p(\boldsymbol{y})
$$ (eq:kld_variational_expanded)

The first term is the variational distribution, the middle term is the joint distribution and the right term is the intractable marginal likelihood [](#eq:bayes_evidence) that we referenced earlier. 

:::{prf:proof}
:class: dropdown
:label: Proof I


Let's look at the KLD measure again with the posterior.

$$
D_{KL}\left[ q(z) || p(z|y)\right] =
\mathbb{E}_{z\sim q(z)} 
\left[ - \log \frac{p(z|x)}{q(z)} \right]
$$

First, we will use log rules to expand the ratio

$$
D_{KL}\left[ q(z) || p(z|y)\right] =
\mathbb{E}_{z\sim q(z)} 
\left[ - \log p(z|x) + \log q(z) \right]
$$

Now, let's plug in the RHS of Bayes posterior outlined in [](#eq:bayes_posterior).

$$
D_{KL}\left[ q(z) || p(z|y)\right] =
\mathbb{E}_{z\sim q(z)} 
\left[ - \log \frac{p(\boldsymbol{z},\boldsymbol{y})}{p(\boldsymbol{y})} + \log q(z) \right]
$$

Again, we use log rules to expand this term

$$
D_{KL}\left[ q(z) || p(z|y)\right] =
\mathbb{E}_{z\sim q(z)} 
\left[ - \log p(\boldsymbol{z},\boldsymbol{y}) + \log p(\boldsymbol{y}) + \log q(z) \right]
$$

Now, we isolate out the marginal likelihood term [](#eq:bayes_evidence) from the rest of the equation and we get

$$
D_{KL}\left[ q(z) || p(z|y)\right] =
\mathbb{E}_{z\sim q(z)} 
\left[ - \log p(\boldsymbol{z},\boldsymbol{y}) + \log q(z) \right] +
\mathbb{E}_{z\sim q(z)} \left[ \log p(\boldsymbol{y}) \right]
$$

We can remove the expectation on the rightmost term because there is no dependency on the latent variable.

$$
D_{KL}\left[ q(z) || p(z|y)\right] =
\mathbb{E}_{z\sim q(z)} 
\left[ - \log p(\boldsymbol{z},\boldsymbol{y}) + \log q(z) \right] +
\log p(\boldsymbol{y})
$$

:::

Looking at [](#eq:kld_variational_expanded), we can rearrange this equation to isolate the expectation on the LHS of the equation. 
This gives us 

$$
\begin{aligned}
\text{ELBO}(q) := &&
\mathbb{E}_{z\sim q(z)}\left[ - \log p(\boldsymbol{z},\boldsymbol{y}) + \log q(z) \right] =
\log p(\boldsymbol{y}) - D_{KL}\left[ q(z) || p(z|y)\right]
\end{aligned}
$$ (eq:elbo)

which is known as the evidence lower bound (ELBO).
This implies that we can maximize the quantity on the RHS of the equation which implies that we are simultaneously i) maximizing the evidence and ii) minimizing the KLD between our variational distribution and the true posterior.

## 3 Perspectives of the ELBO

There are three main ways to look at the ELBO depending upon the literature and application.
The first one is the likelihood perspective, the second one is the flow perspective, and the last one is the variational free energy perspective.
In all three cases, we first need to unpack the ELBO by expanding the joint distribution via Bayes rule outlined in [](#eq:bayes_posterior_factored).
This gives us

$$
\begin{aligned}
\text{ELBO}(q) := &&
\mathbb{E}_{z\sim q(z)}\left[
\underbrace{\log p(\boldsymbol{y}|\boldsymbol{z})}_{\text{Likelihood}} - 

\underbrace{\log p(\boldsymbol{z})}_{\text{Prior}} + 
\underbrace{\log q(z)}_{\text{Variational Dist}} \right]
\end{aligned}
$$ (eq:elbo_expanded)

Below, we outline each of the perspectives.

### Data Fidelity + Prior

If we group the prior term and the variational distribution together, we get

$$
\begin{aligned}
\text{ELBO}(q) := &&
\mathbb{E}_{z\sim q(z)}\left[ 
\log p(\boldsymbol{y}|\boldsymbol{z}) \right]
- 
D_{KL}\left[ 
    q(\boldsymbol{z})||p(\boldsymbol{z})
\right]
\end{aligned}
$$ (eq:elbo_reconstruction)

The first term is the reconstruction loss which measures the expectation of likelihood wrt the variational distribution.
The second term is the KL-Divergence between the prior and the variational distribution.
This formulation is commonly found with Latent Variable models (LVMs) and Variational Autoencoders (VAEs) [{cite}`10.48550/arXiv.1312.6114`].

### Volume Correction

This perspective is more in line with the idea of using transform distributions.
If we group the variational distribution and the likelihood term, we get

$$
\begin{aligned}
\text{ELBO}(q) := &&
\mathbb{E}_{z\sim q(z)}\left[
\log p(\boldsymbol{z})  \right]
+ 
\mathbb{E}_{z\sim q(z)}\left[ 
\log \frac{p(\boldsymbol{y}|\boldsymbol{z})}{q(z)}
 \right]
\end{aligned}
$$ (eq:elbo_vol_correction)

The first term is the *reparameterized probability* via the expectation in the transform distribution.
The second term is the *volume correction factor* or the likelihood contribution.
This formulation was (re-)introduced for the SurVae Flows paper [{cite}`10.48550/arXiv.2007.02731`] where they showcased generalized flows with bijective, surjective, and stochastic transformations.


### Variational Free Energy

Lastly, we have the Variational Free Energy (VFE) formulation which is a very common way to motivate this using Free energy principles which is in part motivated by the Gibbs inequality.
If we group the prior and the likelihood term, we get

$$
\begin{aligned}
\text{ELBO}(q) := &&
\mathbb{E}_{z\sim q(z)}\left[
\log p(\boldsymbol{y},\boldsymbol{z}) \right]
- 
\mathcal{H}
\left[
    q(z) 
\right]
\end{aligned}
$$ (eq:elbo_vfe)

The first term is the energy function which is the variational expectation over the population loss or joint distribution.
The second term is the entropy of the variational distribution which acts as a regularization on the overall complexity of the distribution.
This formulation is common in the Bayesian Learning Rule (BLR) literature [{cite}`10.48550/arXiv.2107.04562,10.48550/arXiv.2303.04397`] as well as the sparse Gaussian process [{cite}`10.48550/arXiv.1606.04820`].


---

# Variational Distribution

We defined the variationa distribution as $q(z|x)$. However, we have many types of variational distributions we can impose. For example, we have some of the following:

* *Delta*, $q(z)=z$
* *Gaussian*, $\mathcal{N}(\boldsymbol{\mu},\boldsymbol{\Sigma})$
* *Laplacian*, $$
* *Mixture Distribution*, $\sum_{k}^{K}\pi_k \mathbb{P}$
* *Bijective Transform* (Flow), $q(z|\tilde{z})$
* *Stochastic Transform* (Encoder, Amortized), $q(z|x)$
* *Conditional*, $q(z|x,y)$

Below we will go through each of them and outline some potential strengths and weaknesses of each of the methods.

---
## Delta Distribution


This is probably the distribution with the least amount of parameters. We set the covariance matrix to $0$, i.e. $\boldsymbol{\Sigma_\theta}:=\mathbf{0}$, and we let all of the mass rest on mean points, $\boldsymbol{\mu_\theta}:=\boldsymbol{\mu}=\mathbf{u}$.

$$
q(z) = \delta(z - \hat{z})
$$

**Note**: Although this is the most trivial variational distribution, it is the most widely used in optimization algorithms because it is equivalent to the MAP estimation (or MLE without any prior) as shown in [{cite}`10.48550/arXiv.1209.4360`].



---
## Simple, $q(z)$

This is the simplest case where we often assume a very simple distribution can describe the distribution.

$$
q(z) = \mathcal{N}(z|\boldsymbol{\mu_\theta},\boldsymbol{\Sigma_\theta})
$$

If we take each of the Gaussian parameters as full matrices, we end up with:

$$
\boldsymbol{\mu_\theta}:=\boldsymbol{\mu} \in \mathbb{R}^D, \hspace{5mm} \boldsymbol{\Sigma_\theta}:=\boldsymbol{\Sigma} \in \mathbb{R}^{D\times D};
$$

For very high dimensional problems, these are a lot of parameters to learn. Now, we can have various simplifications (or complications) with this. For example, we can simplify the mean, $\boldsymbol{\mu}$, to be zero. The majority of the changes will come from the covariance. Here are a few modifications.


**Full Covariance**

This is when we parameterize our covariance to be a full covariance matrix. $\boldsymbol{\Sigma_\theta} := \boldsymbol{\Sigma}$. This is easily the most expensive and the most complex of the Gaussian types.

**Lower Cholesky**

We can also parameterize our covariance to be a lower triangular matrix, i.e. $\boldsymbol{\Sigma_\theta} := \mathbf{L}$, that satisfies the cholesky decomposition, i.e. $\mathbf{LL}^\top = \boldsymbol{\Sigma}$. This reduces the number of parameters of the full covariance by a factor. It also has desireable properties when parameterizing covariance matrices that are computationally attractive, e.g. positive definite.

**Diagonal Covariance**

We can parameterize our covariance matrix to be a diagonal, i.e. $\boldsymbol{\Sigma_\theta} := \text{diag}(\boldsymbol{\sigma})$. This is a very drastic simplification of our model which limits the expressivity. However, there are immense computational benefits For example, a d-dimensional multivariate Gaussian rv with a mean and a diagonal covariance is the same as the product of $d$ univeriate Gaussians.

$$
q(z) = \mathcal{N}\left(\boldsymbol{\mu_\theta}, \text{diag}(\boldsymbol{\sigma_\theta})\right) = \prod_{d}^D \mathcal{N}(\mu_d, \sigma_d )
$$

This is also known as the **mean-field** approximation and it is a very common starting point in practical VI algorithms.

**Low Rank Multivariate Normal**

Another parameterization is a low rank matrix with a diagonal matrix, i.e. $\boldsymbol{\Sigma_\theta} := \mathbf{W}\mathbf{W}^\top + \mathbf{D}$ where $\mathbf{W} \in \mathbb{R}^{D\times d}, \mathbf{D} \in \mathbb{R}^{D\times D}$. We assume that our parameterization can be low dimensional which might be appropriate for some applications. This allows for some computationally efficient schemes that make use of the Woodbury Identity and the matrix determinant lemma.

**Orthogonal Decoupled**

One interesting approach is to map the variational parameters via a subspace parameterization [{cite}`10.48550/arXiv.1809.08820`]. For example, we can define the mean and variance like so:

$$
\begin{aligned}
\boldsymbol{\mu_\theta} &= \boldsymbol{\Psi}_{\boldsymbol{\mu}} \mathbf{a} \\
\boldsymbol{\Sigma_\theta} &= \boldsymbol{\Psi}_{\boldsymbol{\Sigma}} \mathbf{A} \boldsymbol{\Psi}_{\boldsymbol{\Sigma}}^\top + \mathbf{I}
\end{aligned}
$$

This is a bit of a spin off of the Low-Rank Multivariate Normal approach. However, this method takes care and provides a low-rank method for both the mean and the covariance. They argue that we would be able to put more computational effort in the mean function (computationally easy) and less computational effort for the covariance (computationally intensive).

---
## Laplace Approximation


$$
q_{\boldsymbol{\theta}}(x) = p(\hat{x}|y)\exp\left(-\frac{1}{2}(x - \hat{x})\mathbf{S}^{-1}(x-\hat{x}) \right)
$$

where:

$$
x^* = \underset{x}{\text{argmax}} \hspace{1mm} \log p(x|y)
$$

$$
\mathbf{S} = - \boldsymbol{\nabla_\theta}\boldsymbol{\nabla_\theta}p(x|y)|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}}
$$

This method was popularized by [{cite}`10.1090/conm/115/07,10.1162/neco.1992.4.3.415`]



---
## Mixture Distribution

The principal behind this is that a simple base distribution, e.g. Gaussian, is not expressive enough. However, a mixture of simple distributions, e.g. Mixture of Gaussians, will be more expressive. So the idea is to choose simple base distribution and replicate it $k$ times. Then, we then do a normalized weighted summation of each component to produce our mixture distribution.

$$
q(z) = \sum_{k}^K\pi_k \mathbb{P}_k
$$

where $0 \leq \pi_k \leq 1$ and $\sum_{k}^K\pi_k=1$. For example, we can use a Gaussian distribution

$$
p_\theta(z) = \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})
$$

where $\theta = \{\pi_k, \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k \}_k^K$ are potentially learned parameters.. And the mixture distribution will be

$$
q_{\boldsymbol \theta}(\mathbf{z}) = \sum_{k}^K \pi_k \mathcal{N}(\mathbf{z} |\boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)
$$

Again, we are free to parameterize the covariances as flexible or restrictive as possible. For example we can have full, cholesky, low-rank or diagonal. In addition we can *tie* some of the parameters together. For example, we can have the same covariance matrix for every $k^\text{th}$ component, e.g. $\boldsymbol{\Sigma}_k=\boldsymbol{\Sigma}$. Even for VAEs, this becomes a prior distribution which has noticable improvement over the standard Gaussian prior.

**Note**: in principal, a mixture distribution is very powerful and has the ability to estimate any distribution, e.g. univariate with enough components. However, like with most problems, the issue is estimating the best parameters just from observations.


---
## Reparameterized 


---
### Gaussian


---
### Bijective Transformation (Flow)

It may be that the variational distribution, $q$, is not sufficiently expressive enough even with the complex Gaussian parameterization and/or the mixture distribution. So another option is to use a bijective transformation to map the data from a simple base distribution, e.g. Gaussian, to a more complex distribution for our variational parameter, $z$.

$$
\mathbf{z} = \boldsymbol{T_\phi}(\tilde{\mathbf{z}})
$$

We hope that the resulting variational distribution, $q(z)$, acts a better approximation to the data. Because our transformation is bijective, we can

variational parameter, $z$, to a simple base distribution st we ha
$$
q(z) = p_e(\tilde{z})|\boldsymbol{\nabla}_\mathbf{z}\boldsymbol{T_\phi}^{-1}(\mathbf{z})|
$$

where $|\boldsymbol{\nabla}_\mathbf{z} \cdot|$ is the determinant Jacobian of the transformation, $\boldsymbol{T_\phi}$.

---
### Stochastic Transformation (Encoder, Amortization)

Another type of transformation is a stochastic transformation. This is given by $q(z|x)$. In this case, we assume some non-linear. For example, a Gaussian distribution with a parameterized mean and variance via neural networks

$$
q(\mathbf{z}|\mathbf{x}) = \mathcal{N}\left(\boldsymbol{\mu_\phi}(\mathbf{x}), \boldsymbol{\sigma_\phi}(\mathbf{x})\right)
$$

or more appropriately

$$
q(\mathbf{z}|\mathbf{x}) = \mathcal{N}\left(\boldsymbol{\mu}, \text{diag}(\exp (\boldsymbol{\sigma}^2_{\log}) )\right), \hspace{4mm} (\boldsymbol{\mu}, \boldsymbol{\sigma}^2_{\log}) = \text{NN}_{\boldsymbol \theta}(\mathbf{x})
$$

It can be very difficult to try and have a variational distribution that is complicated enough to cover the whole posterior. So often, we use a variational distribution that is conditioned on the observations, i.e. $q(z|x)$. This is known as an encoder because we encode the observations to obey th




---
## Non-Parametric

* Kernels & Stein