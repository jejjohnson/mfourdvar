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

+++ {"part": "abstract"}

This is a top-level document that introduces the Four-Dimensional Variational (4DVar) Formulation from a modern perspective. The purpose of this document is to consolidate all of the 4DVarNet related stuff under one roof. 
It will also serve as a nice springboard for us to use it when explaining 4DVar for different groups, i.e. oceanographers, data assimilation experts and machine learning researchers. 
For the core foundations of 4DVar, this document will host links to the formulation, some specific details involving spatiotemporal discretization, and an introduction to the 4DVarNet algorithm using all of the notation described in the previous two documents. 
For things related to research, there is the document on stochasticity and document consolidating all of the papers that were published (or will be published) related to 4DVar.

+++




## Motivation

We want an abstraction for how we think about the solving problems with modern tools.
The research and software world is enormous and it is very hard to see how everything is connected. 
In many cases, we see instances of people starting with the algorithm and then defining the usecase.
In other cases, we see a lot of instances of people choosing the problem and then
I propose to do it via a problem-oriented approach whereby we build up the necessary abstraction.

**Wide Audience.** 
I want to reach a large audience. 
Nowadays problems are very complicated and it requires many different people from many different disciplines. 
I personally find that we are very bad at communicating with each other irrespective of the audience because we don't take the time or energy to create a common language between each other.

**Easy Entry Point**.
I want there to be a relatively easy entry point for these people to.
I personally find that ML literature tends to be too focused on displaying novelty by highlighting differences rather than similarities.
I want this to highlight similarities rather than differences.
Hopefully it will serve as a springboard for newcomers to get inspired as well as other experts alike to find even more commonalities.

**Software Oriented.** 
I firmly believe software will save science and engineering.
It gives us the necessary computational power to be able to solve new tasks or ask new questions that was impossible before.
However, it's not enough to have such a powerful tool: we need a place to use it.
It's easier to build end-to-end tools once the levels of abstractions have been set.
So having this clean abstraction framework might help people get an idea of how we can make all-inclusive software piece together to build an end-to-end framework.


---
## Framework



### [Task Identification](./framework/tasks.md) (**TODO**)

> There are many geosciences tasks that can be described in terms of ML tasks. The most major tasks include interpolation and forecasting and almost all *tasks* should be somewhere underneath this umbrella. However, there are some other tasks that can occur either. Some could be subtasks that are needed to solve the original task, e.g., denoising, latent embeddings, and conditional density estimation. There are also more "pure" tasks which are less on the application side and more on the *learning* or *discovery* side, e.g. attribution, process discovery, etc. Ultimately, any problem within the geoscience realm can be expressed underneath the Digital Twin umbrella which provides a useful framework to encompass most model-driven developments.


---

### [Problem Structure](./framework/problem.md)


> This provides the core abstraction for how we're going to concretize the problems we want to solve.
> We outline some key components that we need to identity like the Quantity of Interest we wish to estimate, the observations we have access to, the controls we wish to utilize and the overall state we wish to define.
> We also will put this under a single umbrella by using graphical models to represent the relationships between all of the components.
> This will help us to define which pieces we wish to estimate based on what we have and do not have. 
> Many concepts outlined here are heavily inspired by this talk by [Karen Willcox](https://www.youtube.com/watch?v=ZuSx0pYAZ_I&t=2767s) where it presents a similar formulation and proposes the use of Bayesian Graphical Models.


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

### [Estimation Problem](./framework/estimation.md) (**In Progress**)

> This formulation states the learning problem from a Bayesian perspective. 
> We cover the different elements we may want to estimate based on the graphical model we stated above. 
> Namely, we discuss state estimation, parameter estimation, and both (i.e. Bi-Level Optimization).
> We also discuss gradient learning schemes which provide an all-encompassing end-to-end learning framework for learning model parameters, estimating the state space and estimating the path towards the best solution(s).

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

### [Hierarchical Decisions](./framework/problem_decisions.md) (**TODO**)

```{mermaid}
graph LR
    Processes --> Representation
    Representation --> Relationships
    Relationships --> Uncertainty
    Uncertainty --> Solution-Methodology
```

> In order to have a general ontology of how one can include information into a model, we need some standards for how we can describe the decisions we make.
> This outlines the notion of a Hierarchical system where a user can outline all of their assumptions from the idea down to the modeling decisions.
> This attempts at an ontology of generic decisions one has to make to create a model and find a solution.
> This includes defining the *processes* involved, choosing an approprate *representation* based on the data and the resources, choosing how the *process relationships*, including the *uncertainty* through every level, and the *solution* methodology chosen.
> Many concepts here stem from this excellent talk by [Hoshin Gupta](https://www.youtube.com/watch?v=eH6vwiukIsA&t=3541s&pp=ygUYaW5mb3JtYXRpb24gaG9zaGluIGd1cHRh) that outlines an instance of Hierarchical system of model choices one can use.
> This section also serves as a precursor to the following section where we go into more details.




---
## Model Choices

These are things that we need to decide as we are constructing our model and learning framework.
A fancier way to say this is *Hierachical Sequence of Decisions*.  
This is motivated by an excellent talk by [Hoshin Gupta](https://www.youtube.com/watch?v=eH6vwiukIsA&t=3541s&pp=ygUYaW5mb3JtYXRpb24gaG9zaGluIGd1cHRh) about the general theory of learning with models and data.


### [Data + Model Representation](./model_choices/discretization.md) (**TODO**)

> There is an intermediate step which is often neglected in the case of interpolation and forecasting problems. This involes how the spatiotemporal domain differs between the state, the QOI and the observations.


### [Physics Informed](./model_choices/physics_informed.md) (**TODO**)

> There is a lot of talk throughout the literature about physics informed (or scientific machine learning). There are many ways we can incorporate physics into the 4DVar framework and I think it is worth mentioning explicitly how we can do so. This section will highlight the three main ways we can add physical knowledge into the 4DVar setting, i.e. data, representation + architecture, and the loss function.


### [Uncertainty](./model_choices/uncertainty.md) (**In Progress**)

> There are many connections and extensions to be made to incorporate stochasticity into the system. This document explores a few of them.



---
## Examples (**In Progress**)

> Some examples of how this can be used in various contexts. The first biggest choice we can make is the representation of the QOI and observations we are going to encounter and how do we transform between these representations. The second biggest decision we can make is whether to use an autoregressive model that propagates the model forward in time or a *memory* model that ingests the entire spatiotemporal field


### [State Estimation](./examples/state_estimation.md) (**In Progress**)

### [Parameter Estimation](./examples/param_estimation.md) 

### [BiLevel Optimization](./examples/bilevel_estimation.md) (**TODO**)

### [Gradient Learning](./examples/gradient_learning.md) 

---
## Dissimentation (**In Progress**)

> This consolidates all of the resources necessary to get started with 4DVarNet including tutorials, literature and databases.

### [Code](./resources/code.md) (**In Progress**)

### [Papers](./resources/papers.md) (**TODO**)
