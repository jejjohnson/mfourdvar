---
title: Discretization
subject: Modern 4DVar
subtitle: The Importance of Discretization
short_title: Discretization
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


We consider the trifecta for determining inverse problems: 
1. the latent variable which acts as the hidden state space
2. the quantity of interest which we are interested in estiamting
3. the observations which we condition on to guide us in estimating the latent variable.

In summary, we write these fields mathematically as

$$
\begin{aligned}
\text{Latent Variable}: && 
\boldsymbol{z}=\boldsymbol{z}(\vec{\mathbf{x}},t), && \vec{\mathbf{x}}\in\boldsymbol{\Omega}_z\subseteq\mathbb{R}^{D_s} && 
t\in\mathcal{T}_{z}\in\mathbb{R}^{D_t}\\
\text{Quantity of Interest}: && 
\boldsymbol{u}=\boldsymbol{u}(\vec{\mathbf{x}},t) &&
\vec{\mathbf{x}}\in\boldsymbol{\Omega}_u\subseteq\mathbb{R}^{D_s} && 
t\in\mathcal{T}_{u}\in\mathbb{R}^{D_t}\\
\text{Observation}: && 
\boldsymbol{y}=\boldsymbol{y}(\vec{\mathbf{x}},t) &&
\vec{\mathbf{x}}\in\boldsymbol{\Omega}_y\subseteq\mathbb{R}^{D_s} && 
t\in\mathcal{T}_{y}\in\mathbb{R}^{D_t}\\
\end{aligned}
$$

where each of these fields are mappings between the coordinates of the respective domains and the scalar or vector value of the field. However, this notation implies a continuous form of each of the fields which is not always available nor necessary. In addition, 

# Temporal Discretization

We look at the temporal coordinates

$$
t \in \mathcal{T} \subseteq \mathbb{R}^{D_t}
$$

A simple example would be to have some time units ranging from zero to some constant like

$$
\mathcal{T}=[0, T]
$$

however, we can have other ways of encoding time depending upon the situation. See the *encodings* section below.




# Spatial Discretization



$$
\vec{\mathbf{x}} \in \boldsymbol{\Omega} \subseteq \mathbb{R}^{D_s}
$$

$$
\boldsymbol{\Omega}:=\boldsymbol{\Omega}(t)
$$

# Between Spaces

In many cases, we are not operating on the same spatiotemporal domain. This is often the case when we are dealing with observations.

### Case I: Same Time, Same Space

$$
\begin{aligned}
\boldsymbol{\Omega}_z &= \boldsymbol{\Omega}_u \\
t_z &= t_u
\end{aligned}
$$

This is the common framework for simulated data.

### Case II: Same Time, Differnt Space

$$
\begin{aligned}
\boldsymbol{\Omega}_z &\neq \boldsymbol{\Omega}_u \\
t_z &= t_u
\end{aligned}
$$

This is the common problem for interpolation and extrapolation problems.


### Case III: Different Time, Different Space


$$
\begin{aligned}
\boldsymbol{\Omega}_z &\neq \boldsymbol{\Omega}_u \\
t_z &\neq t_u
\end{aligned}
$$

This is common for forecasting problems whereby we have a latent space that  we are confident in but the QOI of interest that we want to predict lies in a different spatiotemporal domain.

# Encodings


Time can be difficult to encode into a neural network as there are some variables that are cyclic by nature. For example, hours, months, and days of the year are on a cycle. Seasons can also be on a cycle. One option would be to remove these trends from the 

However, we can have some more sophisticated encodings like sinusoidal encodings to encode cyclic features, e.g.

$$
\text{Encoder}(t) =
\left[
\sin\left(\frac{2\pi t}{T}\right), 
\cos\left(\frac{2\pi t}{T}\right)
\right]^\top
$$

or we can do some more sophisticated encoders like sinusoidal embeddings.