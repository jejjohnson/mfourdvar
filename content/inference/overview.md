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
\sum_{n=1}^N \boldsymbol{D}(z;\boldsymbol{\theta}) +
\boldsymbol{R}(z;\boldsymbol{\theta})
$$

where $D$ is a data fidelity term and $R$ is a regularization term.


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





---

:::{prf:proof}
:class: dropdown



We want to find the optimal soft predictor by solving the problem of minimizing the population log-loss. 
However, 

$$
q^*(\cdot|\cdot) = 
\underset{q(\cdot|\cdot)}{\text{argmin}} \hspace{2mm}
\mathbb{E}_{(z,y)\sim p(z,y)}
\left[ -\log q(z|y)\right]
$$

Looking at the Bayes theorem, we con deconstruct this population loss as a conditional distribution.

$$
p(z,y) = p(z|y)p(y)
$$

We can use the law of iterated expectations to use this as follows

$$
q^*(\cdot|\cdot) = 
\underset{q(\cdot|\cdot)}{\text{argmin}} \hspace{2mm}
\mathbb{E}_{y\sim p(y)}
\underbrace{
    \left[\mathbb{E}_{z\sim p(z|y)}
\left[ -\log q(z|y)\right]
\right]}_{\text{Cross Entropy}}
$$

We know that the distribution of the observation data doesn't change and we have...
So we can write this in terms of the cross entropy alone

$$
q^*(\cdot|y) = 
\underset{q(\cdot|y)}{\text{argmin}} \hspace{2mm}
\mathbb{E}_{z\sim p(z|y)}
\left[ -\log q(z|y)\right]
$$

which is the cross entropy between the true posterior and the optimal soft predictor. 
This is a measure of "regret" or excess loss. whereby the optimal soft predictor is when this is equal, i.e. $q^*(z|y)=p(z|y)$.
The log-loss measures the "surprise" experienced by the predictor when observing $y=y$ given $z=z$.
The surprise is higher if the output is less expected

:::


## Bayesian Learning Rule


$$
q^*(z|y) = 
\underset{q(u|y)}{\text{argmin}} \hspace{2mm}
\mathbb{E}_{}
\left[ p(y|z) \right] +
D_{KL}
\left[ q(z|y) || p(z|y)\right]
$$
