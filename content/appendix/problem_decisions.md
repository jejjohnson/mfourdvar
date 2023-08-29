---
title: Hierarchical Sequence of Decisions
subject: Modern 4DVar
subtitle: How we choose how to include information at every step
short_title: Problem Choices
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



```{mermaid}
graph LR
    Processes --> Representation
    Representation --> Relationships
    Relationships --> Uncertainty
    Uncertainty --> Solution-Methodology
```


## Process Identification

In this step, we create a representation or schematic all of the processes that we believe are necessary to solve the task we are interested in. The idea is that we identify the processes that we want and the processes that we have access to. Some basic questions to ask ourselves:

1. What knowledge do we want to encode?
2. What processes do we want to include?
3. What observations do we have access to?

A nifty way to do this is to use a (probabilistic) graphical model.

1. We label the (un-)observable processes as nodes of the graph.
2. We label the connections between the processes as (directional) edges connecting the nodes of the graph.


**Note**: If you come from a more physical processes background then it is very natural to think about the process relationships in more detail in order to garner your thoughts to an appropriate schematic to represent them.

### Processes

The processes are the concrete entities that represent the variables we wish to include. 
There are many things we may want to include as processes.
Some examples include:

* Variables
* Physical Laws (conservation of mass, energy and momentum)
* physical processes
* system geometries
* material properties

Now to represent these things in the graphical representation, we can use the following rubric.


| Description  | Observed |
|:------------|:-----|
| Processes | Observable/Unobservable |
| What you want  | Unobservable |
| What you can measure | Observable |
| Auxillary Processes | Observable\Unobservable |


### Relationships

The relationships are what map one process to another. 
There is a lot of flexibility in the 


* **Independent** - there is no presumed relationship between two processes
* **Bidirection** - there is a presumed relationship between two processes but it is not clear which way is the causality; possibly a correlation
* **Dependent** - there is a presumed direction of causality between two processes


### Hypothesis

In doing so, we are enforcing laws which restricts the possible trajectories.
So overall, we create a system hypothesis

$$
\begin{aligned}
\text{Process Hypthesis}: && \mathcal{H}_p
\end{aligned}
$$


## System Representation

In order to do computation, we need to have a representation of the processes even if it is simply to store the bits and pieces.

* What is a sufficiently complex, finite dimensional, spatiotemporally organized representation of the sub-system architecture
* What are some computation/memory constraints?
* What scales do we wish to resolve? Can they be captured at the specified resolution?
* What does my data/rpcesses look like?

Overall we need to do the following:

* Choose a coordinate system
* Choose a domain and discretization
* Choose a representation

$$
\begin{aligned}
\text{Spatial Coordinates}: && \vec{\mathbf{x}} \in \Omega \sub \mathbb{R}^{D_s} \\
\text{Temporal Coordinates}: && t \in \mathcal{T} \sub \mathbb{R}^+
\end{aligned}
$$


### Example

We need to choose a scale and a spatiotemporal structure of the state-space elements.
We need to choose a system to represent the coordinates.
For example, the spatial coordinates could be in the Cartesian space or perhaps the spherical space.
We also need a system to represent the time evolution.
For example, we could have discrete time or (near) continuous time or cyclic time, e.g. hours, months, years, seasons, etc.


### Hypothesis

In doing so, this further restricts the trajectories and determines the spatiotemporal variability..
So overall, we create a system hypothesis

$$
\begin{aligned}
\text{Process Hypothesis}: && \mathcal{H}_{sys}
\end{aligned}
$$



## Process Parameterization


Now, we want to do computation but we cannot do it because don't have any equations/operations!

* What mathematical forms to use to flow between the nodes?
* What parameters (artefacts from assumptions) are introduced?
* What parameterizations are introduced?


### Examples


**Neural Field**. 
We can parameterize a field directly via some parameters

$$
\boldsymbol{z}(\vec{\mathbf{x}},t) = \boldsymbol{f}
\left( \vec{\mathbf{x}},t,\boldsymbol{\theta} \right) 
$$

**Operator**.
We learn an operator from one process to another in the corresponding domain.

$$
\boldsymbol{u}(\boldsymbol{\Omega},t) = \boldsymbol{T}
\left( 
  \boldsymbol{z}\left(
    \boldsymbol{\Omega},t
    \right), \boldsymbol{\Omega}, t; \boldsymbol{\theta}
\right)
$$

**Flow Map**.
We can learn a flow map that maps the 

$$
\partial_t\boldsymbol{z}(\boldsymbol{\Omega},t) = \boldsymbol{F}
\left( 
  \boldsymbol{z}\left(
    \boldsymbol{\Omega},t
    \right), \boldsymbol{\Omega}, t; \boldsymbol{\theta}
\right)
$$

### Hypothesis

In doing so, this further restricts the trajectories and introduces "tunable" parameters.
So overall, we create a parameterization hypothesis

$$
\begin{aligned}
\text{Process Parameterization}: && \mathcal{H}_{pp}
\end{aligned}
$$


---

## Uncertainty

> What we know that we do not know precisely (or not all)?

What uncertainties are important, and how to represent them mathematically?

### Hypothesis

In doing so, this characterizes and quantities "known knowns" and "known unknowns".
So overall, we create a uncertainty hypothesis

$$
\begin{aligned}
\text{Process Uncertainty}: && \mathcal{H}_{\epsilon}
\end{aligned}
$$


---
## Identify the Problem

**Inference** - estimate/detect a quantity and/or parameters given some observations.

**Learning** - choosing the best model hypothesis and/or parameters that maximizes the data likelihood.



---
## Solution Procedure

> Problem for "solving" the mathematical model

How to integrate the resulting spatiotemporal system of stochastic physics-informed equations?

$$
\mathcal{H} = \left\{ 
  \mathcal{H}_{p},\mathcal{H}_{sys},\mathcal{H}_{pp},\mathcal{H}_{\epsilon}
\right\}
$$

**This converts the model info and input info into specific (uncertain) trajectories**.

### Evaluating Integrals

* Sampling - MC, MCMC, IS, IWS, HMC
* Closed-Form (Linear + Exponential Familty + Conjugation)
* Bayesian Learning Rule - Optimization
* Variational Inference - Optimization