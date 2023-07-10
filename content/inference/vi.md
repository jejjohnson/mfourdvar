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
