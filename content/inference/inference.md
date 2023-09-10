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
    VI: Variational Inference
---
## Overview

We have isolated the problems we wish to address: state estimation,We traditionally jump straight into



---
## Quick Overview

**Variational Inference**. 
In this section, we predominantly look at variational inference (VI) because it offers us a way to solve the difficult integral problems by using optimization schemes.
In fact, the most widely used method for solving these optimization schemes is the MAP method which approximates the variational distribution with a Delta distribution.

**Optimization**. 
As shown in the VI section, we transform the Bayesian inference problem of integration into one of optimization.
In this section, we give a crash-course in some of the most popular optimization schemes available as well as some pros and cons for each.

**Bayesian Learning Rule**. 
In this section, we will generalize the VI and optimization schemes under a single umbrella: the Bayesian Learning Rule (BLR).
This is very helpful to give us a common framework to be able to connect the methods as well as invent new ones.

**Bi-Level Optimization**.
In this section, we look at how we can use ML to optimize both the state **and** the parameters.
This is underneath the umbrella of bi-level optimization schemes whereby we minimize the inner-level objective and apply *argmin differentiation* to minimize the outer-level objective.

**Meta-Learning**.
As shown by all of these methods, we are always dealing with optimization schemes. 
However, for state estimation in particular, this can be very expensive and memory consuming because we are dealing with high-dimensional state-space systems.
In addition, we need a quick way to do transfer learning


---
## When to use which one?

**VI Can Give Accurate Answers**. The family can determine how accuracy answers you can obtain. Example: MF isn't very good. However, it's very scalable. I'll get many things wrong but some things correct. The objective function can (forward or reverse KL) also influence.

**You Don't Need Accurate Inference**. More Data + Sophisticated Model, Less Accurate Inference, e.g. Deep learning. You're on a computational budget.

**Open Question**. Which regime we're in? How do we diagnosis VI?

**Bayesian Workflow**. 
You use cheap computation in the beginning, you refine the model, you repeat with cheap inference. 
Once the Model is more refined, then one can run the heavy sampling methods like MCMC.

**Source**: This is taken from the [podcast](https://www.youtube.com/watch?v=wEKqznbHHQw). 

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


