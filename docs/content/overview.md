---
title: Overview
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

This is a top-level document that introduces the Four-Dimensional Variational (4DVar) Formulation from a modern perspective. The purpose of this document is to consolidate all of the 4DVarNet related stuff under one roof. 
It will also serve as a nice springboard for us to use it when explaining 4DVar for different groups, i.e. oceanographers, data assimilation experts and machine learning researchers. 
For the core foundations of 4DVar, this document will host links to the formulation, some specific details involving spatiotemporal discretization, and an introduction to the 4DVarNet algorithm using all of the notation described in the previous two documents. 
For things related to research, there is the document on stochasticity and document consolidating all of the papers that were published (or will be published) related to 4DVar.


## Motivation

4DVarNet is an excellent framework for solving many different problems.
However, 

This stems from the paper by [Kapteyn et al, 2021](doi:10.1038/s43588-021-00069-0) does a great explanation of how we can look at


---
## [Formulation](./formulation.md)

> This gives the formulation for how we think about a state space being a link between the quantities of interest and the observations.

$$
\begin{aligned}
\text{Quantity of Interest}: &&
\boldsymbol{u} = \boldsymbol{u}(\vec{\mathbf{x}},t)
&& \boldsymbol{u}: \boldsymbol{\Omega}_u \times \mathcal{T}_u \rightarrow \mathbb{R}^{D_u} \\
\text{State Space}: &&
\boldsymbol{z} = \boldsymbol{z}(\vec{\mathbf{x}},t),
&& \boldsymbol{z}: \boldsymbol{\Omega}_z \times \mathcal{T}_z \rightarrow \mathbb{R}^{D_z} \\
\text{Observations}: &&
\boldsymbol{y} = \boldsymbol{y}(\vec{\mathbf{x}},t)
&& \boldsymbol{y}: \boldsymbol{\Omega}_y \times \mathcal{T}_y \rightarrow \mathbb{R}^{D_y}
\end{aligned}
$$



---

## [Learning](https://hackmd.io/@jejjohnson/HypHQ3t_h) (**In Progress**)

> This formulation states the learning problem from a Bayesian perspective. We cover state estimation, parameter estimation, bi-level optimization (both param and state), and also objective-based learning schemes. We also cover gradient learning schemes.

$$
\begin{aligned}
\text{Parameter Estimation}: &&
\boldsymbol{\theta}^* &= 
\underset{\boldsymbol{\theta}}{\text{argmin}}
\hspace{2mm}
\boldsymbol{L}(\boldsymbol{\theta};\mathcal{D}) \\
\text{State Estimation}: &&
\boldsymbol{z}^*(\boldsymbol{\theta}) &=
\underset{\boldsymbol{z}}{\text{argmin}}
\hspace{2mm}
\boldsymbol{J}(\boldsymbol{z};\boldsymbol{\theta}) \\
\text{Gradient Learning}: &&
\boldsymbol{z}^{(k+1)} &= \boldsymbol{z}^{(k)} + \boldsymbol{g}_k \\
&& [\boldsymbol{g}_k, \boldsymbol{h}_{k+1}] &= \boldsymbol{g}(\boldsymbol{\nabla_z}\boldsymbol{J},\boldsymbol{h}_k, k; \boldsymbol{\phi})
\end{aligned}
$$


---
## [Discretization](https://hackmd.io/@jejjohnson/rkihPJvu3) (**TODO**)

> There is an intermediate step which is often neglected in the case of interpolation and forecasting problems. This involes how the spatiotemporal domain differs between the state, the QOI and the observations.

---
## [Physics Informed](https://hackmd.io/@jejjohnson/HJTA_aFd3) (**TODO**)

> There is a lot of talk throughout the literature about physics informed (or scientific machine learning). There are many ways we can incorporate physics into the 4DVar framework and I think it is worth mentioning explicitly how we can do so. This section will highlight the three main ways we can add physical knowledge into the 4DVar setting, i.e. data, representation + architecture, and the loss function.

---
## [Stochasticity](https://hackmd.io/@jejjohnson/Sy4MO1Puh) (**In Progress**)

> There are many connections and extensions to be made to incorporate stochasticity into the system. This document explores a few of them.

---
## [Tasks](https://hackmd.io/@jejjohnson/BJERqTtu2) (**TODO**)

> There are many geosciences tasks that can be described in terms of ML tasks. Some major tasks include interpolation and forecasting. Some minor tasks include denoising, latent embeddings, and conditional density estimation.

---
## Examples (**In Progress**)

> Some examples of how this can be used in various contexts. The first biggest choice we can make is the representation of the QOI and observations we are going to encounter and how do we transform between these representations. The second biggest decision we can make is whether to use an autoregressive model that propagates the model forward in time or a *memory* model that ingests the entire spatiotemporal field


### [State Estimation](https://hackmd.io/@jejjohnson/HyN481Duh) (**In Progress**)

### Parameter Estimation (**TODO**)

### [BiLevel Optimization](https://hackmd.io/@jejjohnson/Hyeokfi_n) (**TODO**)

### Gradient Learning (**TODO**)

---
## [Dissimentation](https://hackmd.io/ntIWvyBwQ4ambCr470p6Gg) (**In Progress**)

> This consolidates all of the resources necessary to get started with 4DVarNet including tutorials, literature and databases.

## [4DVarNet](https://hackmd.io/@jejjohnson/HkahUJv_n) (**TODO**)

> An explanation of the ultimate algorithm which is currently beating all of the records for Sea Surface Height Interpolation.



## Misc