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

This document goes over the Bayesian formulation in relation to some of the estimation and learning problems we have identified earlier.

* State and Observations
* Parameters and Data
* State, Parameters & Data
* Temporal State and Observations
* Temporal State, Parameters & Data

---

## State & Observations

In this case, we are interested in


**Joint Distribution**

$$
p(\boldsymbol{z},\boldsymbol{y}) =
p(\boldsymbol{y}|\boldsymbol{z})p(\boldsymbol{z}) =
p(\boldsymbol{z}|\boldsymbol{y})p(\boldsymbol{y})
$$

**Posterior**

$$
p(\boldsymbol{z}|\boldsymbol{y}) =
\frac{p(\boldsymbol{y}|\boldsymbol{z})p(\boldsymbol{z})}{p(\boldsymbol{y})}
$$

**Evidence**

$$
p(\boldsymbol{y}) =
\int p(\boldsymbol{y}|\boldsymbol{z})p(\boldsymbol{z}) d\boldsymbol{z}
$$

**Posterior Predictive Distribution**

$$
p(\boldsymbol{u}|\boldsymbol{z}) =
\int p(\boldsymbol{u}|\boldsymbol{z})
p(\boldsymbol{z}|\boldsymbol{y})
d\boldsymbol{z}
$$

---

## Parameters & Data


Given some data $\mathcal{D} = \left\{ u_n, z_n\right\}_{n=1}^N$

**Joint Distribution**

$$
p(\boldsymbol{\theta},\mathcal{D}) =
p(\boldsymbol{\theta}|\mathcal{D})
p(\mathcal{D}) =
p(\mathcal{D}|\boldsymbol{\theta})
p(\boldsymbol{\theta})
$$

**Posterior**

$$
p(\boldsymbol{\theta}|\mathcal{D}) =
\frac{p(\mathcal{D}|\boldsymbol{\theta})}{p(\mathcal{D}) }
$$

**Evidence**

$$
p(\mathcal{D}) = 
\int p(\mathcal{D}|\boldsymbol{\theta})
p(\boldsymbol{\theta})
d\boldsymbol{\theta}
$$

**Posterior Predictive Distribution**

$$
p(\boldsymbol{u}|\boldsymbol{z},\boldsymbol{\theta}) =
\int p(\boldsymbol{u}|\boldsymbol{z},\boldsymbol{\theta})
p(\boldsymbol{\theta}|\mathcal{D})
d\boldsymbol{\theta}
$$

---

## State, Parameters & Data

**Joint Distribution**

$$
p(\boldsymbol{z},\boldsymbol{\theta},\boldsymbol{y}) =
p(\boldsymbol{z}|\boldsymbol{y},\boldsymbol{\theta})
p(\boldsymbol{y}) =
p(\boldsymbol{y}|\boldsymbol{z},\boldsymbol{\theta})
p(\boldsymbol{z}|\boldsymbol{\theta})
p(\boldsymbol{\theta})
$$

**Posterior**

$$
p(\boldsymbol{z}|\boldsymbol{\theta}|\boldsymbol{y}) =
\frac{1}{Z}
p(\boldsymbol{z}|\boldsymbol{z},\boldsymbol{\theta})
p(\boldsymbol{z}|\boldsymbol{\theta})
p(\boldsymbol{\theta})
$$

**Evidence**

$$
\mathbf{Z} =
\int p(\boldsymbol{y}|\boldsymbol{z},\boldsymbol{\theta})
p(\boldsymbol{z}|\boldsymbol{\theta})
p(\boldsymbol{\theta})
d\boldsymbol{\theta}
$$

**Posterior Predictive Distribution**

$$
p(\boldsymbol{u}|\boldsymbol{z},\boldsymbol{\theta}) =
\int p(\boldsymbol{u}|\boldsymbol{z},\boldsymbol{\theta})
p(\boldsymbol{z}|\boldsymbol{\theta}|\boldsymbol{y})
d\boldsymbol{z}
$$


---

## State-Space Model and Observations

```{mermaid}
graph TD
    z0 --> z1 --> z2
    z1 --> y1
    z2 --> y2
    z1 --> u1
    z2 --> u2
```

In this example, we have a state space model and some observations.
So we break up the **Joint Distribution** into a temporal discretization.

$$
p(\boldsymbol{z},\boldsymbol{y}|\boldsymbol{\theta}) =
p(\boldsymbol{z}_{0:T},\boldsymbol{y}_{1:T}|\boldsymbol{\theta})
$$


So our new Bayesian decomposition of the **joint distribution** is given by

$$
\begin{aligned}
p(\boldsymbol{z}_{0:T},\boldsymbol{y}_{1:T}|\boldsymbol{\theta}) &=
p(\boldsymbol{y}_{1:T}|\boldsymbol{z}_{0:T},\boldsymbol{\theta})
p(\boldsymbol{z}_{0:T}|\boldsymbol{\theta}) \\
&=
p(\boldsymbol{z}_{0:T}|\boldsymbol{y}_{1:T},\boldsymbol{\theta})
p(\boldsymbol{y}_{1:T})
\end{aligned}
$$

where we have a prior distribution defined as a dynamical model, a likelihood model for the measurements (and we will have a normalization constant).


Here, we have the following assumptions for the relationships

$$
\begin{aligned}
\text{Prior}: && \boldsymbol{z}_0 
&\sim p(\boldsymbol{z}_0|\boldsymbol{\theta}) \\
\text{Transition}: && \boldsymbol{z}_{t}
&\sim p(\boldsymbol{z}_{t}|\boldsymbol{z}_{t-1},\boldsymbol{\theta}) \\
\text{Emission}: && \boldsymbol{y}_t
&\sim p(\boldsymbol{y}_t|\boldsymbol{z}_t,\boldsymbol{\theta})
\end{aligned}
$$



So we can decompose the distributions listed above as

$$
p(\boldsymbol{z}_{0:T},\boldsymbol{y}_{1:T}|\boldsymbol{\theta})= p(\boldsymbol{z}_0)
\prod_{t=1}^Tp(\boldsymbol{z}_t|\boldsymbol{z}_{t-1})
\prod_{t=1}^Tp(\boldsymbol{y}_t|\boldsymbol{z}_t)\\
$$

**State Posterior**

$$
\begin{aligned}
p(\boldsymbol{z}_{0:T}|\boldsymbol{y}_{1:T},\boldsymbol{\theta}) &=
\frac{p(\boldsymbol{y}_{1:T}|\boldsymbol{z}_{0:T},\boldsymbol{\theta})
p(\boldsymbol{z}_{0:T}|\boldsymbol{\theta})}{p(\boldsymbol{y}_{1:T})} 
\end{aligned}
$$

**Evidence**

$$
\begin{aligned}
p(\boldsymbol{y}_{1:T}) &= \int
p(\boldsymbol{y}_{1:T}|\boldsymbol{z}_{0:T},\boldsymbol{\theta})
p(\boldsymbol{z}_{0:T}|\boldsymbol{\theta})
d\boldsymbol{z}_{0:T} \\
&= \int p(\boldsymbol{z}_0)
\prod_{t=1}^Tp(\boldsymbol{y}_t|\boldsymbol{z}_t)
d\boldsymbol{z}_t
\end{aligned}
$$


**Predictive Posterior Distribution**

$$
p(u_{1:T}|z_{0:T}) = \int
p(u_{1:T}|z_{1:T})p(z_{1:T}|y_{1:T},\theta)
p(z_0|\theta)dz_{0:T}
$$

**Other Quantities**

$$
\begin{aligned}
\text{Filtering Dist}: && p(z_t|y_{1:t}) \\
\text{Predictive Dist}: && p(z_{t+\tau}|y_{1:t}) \\
\text{Smoothing Dist}: && p(z_t|y_{1:T})
\end{aligned}
$$


---

## Parameters, State-Space Model, & Observations

In this example, we have a state space model and some observations.
So we break up the **Joint Distribution** into a temporal discretization.

$$
p(\boldsymbol{z},\boldsymbol{y},\boldsymbol{\theta}) =
p(\boldsymbol{z}_{0:T},\boldsymbol{y}_{1:T},\boldsymbol{\theta})
$$


So our new Bayesian decomposition of the **joint distribution** is given by

$$
\begin{aligned}
p(\boldsymbol{z}_{0:T},\boldsymbol{y}_{1:T}|\boldsymbol{\theta}) &=
p(\boldsymbol{y}_{1:T}|\boldsymbol{z}_{0:T},\boldsymbol{\theta})
p(\boldsymbol{z}_{0:T}|\boldsymbol{\theta})p(\theta) \\
&=
p(\boldsymbol{z}_{0:T}|\boldsymbol{y}_{1:T},\boldsymbol{\theta})
p(\boldsymbol{y}_{1:T})
\end{aligned}
$$

where we have a prior distribution defined as a dynamical model, a likelihood model for the measurements (and we will have a normalization constant).


Here, we have the following assumptions for the relationships

$$
\begin{aligned}
\text{Prior Parameters}: && \boldsymbol{\theta}
&\sim p(\boldsymbol{\theta}) \\
\text{Prior State}: && \boldsymbol{z}_0 
&\sim p(\boldsymbol{z}_0|\boldsymbol{\theta}) \\
\text{Transition}: && \boldsymbol{z}_{t}
&\sim p(\boldsymbol{z}_{t}|\boldsymbol{z}_{t-1},\boldsymbol{\theta}) \\
\text{Emission}: && \boldsymbol{y}_t
&\sim p(\boldsymbol{y}_t|\boldsymbol{z}_t,\boldsymbol{\theta})
\end{aligned}
$$



So we can decompose the distributions listed above as

$$
p(\boldsymbol{z}_{0:T},\boldsymbol{y}_{1:T}|\boldsymbol{\theta})= 
p(\theta)p(\boldsymbol{z}_0|\theta)
\prod_{t=1}^Tp(\boldsymbol{z}_t|\boldsymbol{z}_{t-1},\theta)
\prod_{t=1}^Tp(\boldsymbol{y}_t|\boldsymbol{z}_t,\theta)\\
$$

**Joint Posterior**

$$
\begin{aligned}
p(\boldsymbol{z}_{0:T},\boldsymbol{\theta}|\boldsymbol{y}_{1:T}) &=
\frac{p(\boldsymbol{y}_{1:T}|\boldsymbol{z}_{0:T},\boldsymbol{\theta})
p(\boldsymbol{z}_{0:T}|\boldsymbol{\theta})p(\theta)}{p(\boldsymbol{y}_{1:T})} 
\end{aligned}
$$

**Evidence**

$$
\begin{aligned}
p(\boldsymbol{y}_{1:T}) &= \int\int
p(\boldsymbol{y}_{1:T}|\boldsymbol{z}_{0:T},\boldsymbol{\theta})
p(\boldsymbol{z}_{0:T}|\boldsymbol{\theta})p(\theta)
d\boldsymbol{z}_{0:T}d_\theta \\
&= \int\int p(\theta)p(\boldsymbol{z}_0)
\prod_{t=1}^Tp(\boldsymbol{y}_t|\boldsymbol{z}_t)
d\boldsymbol{z}_td\theta
\end{aligned}
$$


**Predictive Posterior Distribution (State)**

$$
p(\theta|y_{1:T}) = \int p(z_{0:T},\theta|y_{1:T})p(\theta)dz_{0:T}
$$

**Predictive Posterior Distribution (Parameters)**

$$
p(z_{0:T}|y_{1:T}) = \int p(z_{0:T},\theta|y_{1:T})p(\theta)d\theta
$$

**Predictive Posterior Distribution (QoI)**

$$
\begin{aligned}
\text{State \& Parameters}: &&
p(u_{1:T}|z_{0:T},\theta) &= \int 
p(u_{1:T}|z_{0:T},\theta)
p(\boldsymbol{z}_{0:T},\boldsymbol{\theta}|\boldsymbol{y}_{1:T})p(\theta)
dz_{0:T}d\theta\\
\text{State}: &&
p(u_{1:T}|z_{0:T}) &= \int 
p(u_{1:T}|z_{0:T})
p(\boldsymbol{z}_{0:T}|\boldsymbol{y}_{1:T})
dz_{0:T}\\
\text{Parameters}: &&
p(u_{1:T}|\theta) &= \int 
p(u_{1:T}|\theta)
p(\theta|\boldsymbol{y}_{1:T})
d\theta\\
\end{aligned}
$$
