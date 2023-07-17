---
title: OceanBench Overview
subject: Modern 4DVar
subtitle: An agnostic framework for benchmarking geoscience applications
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
    OSE: Observing System Experiments
    OSSE: Observing System Simulation Experiments
    SSH: Sea Surface Height
    ML: Machine Learning
---

> "OceanBench is a framework for co-designing learning-driven high-level experiments from ocean models, reanalysis, and observations.
> It consists of an end-to-end framework for piping data from its raw form to an ML-ready state and from model outputs to interpretable quantities.
> We regard OceanBench as a key facilitator for the uptake of MLOPs tools and research for ocean-related tasks and case studies with genuine ocean data.

## Motivation

```{mermaid}
graph LR
    Observation-Data --> ML-Ready-Data
    Simulation-Data --> ML-Ready-Data
    Assimilation-Data --> ML-Ready-Data
    ML-Ready-Data --> ML-Ideation
    ML-Ideation --> ML-Ideation
    ML-Ideation --> ML-Tool
    ML-Tool --> MLOPs
    ML-Tool --> Research
    ML-Tool --> Evaluation
    MLOPs --> Product
```

There are many facets to utilizing ML tools in an operational setting.
A lot of emphasis is spent on the ML methods used to solve the problem.
We argue that this is the smallest part of the entire chain.
The most important parts include: 

* how we get the data into a format that is easily digestible for a ML setting
* how do we evaluate the proposed ML-tool for real world problems
* how we incorporate the ML tool into an operational setting

And most importantly, how do we construct a consistent, reproducible framework where non-operational experts can focus only on the task a single task at hand.
By having a system they can plug-in-play, this will make the results of their efforts more meaningful.

We also hope to bridge the gap between the research setting and the operational settings.
In many cases, researchers tend to work on expertly-contrived solutions but they often do not make the jump to real problems.
This is completely understandable because there are many
We can work directly domain experts with operational expertise to design


---
## Use Cases

**ML Researchers**. 

**Domain Experts**. We hope to reach domain experts by providing a concrete platform to buildSome of the most fruitful contributions can be:

1. Experimental Design -
2. Evaluation Procedures - Experts can help incorporate better and more meaningful metrics that ML experts can strive to reach.
3. Preprocessing Techniques - Experts can help , e.g. coordinate/domain transformations, denoising, variable transformations, etc.


**Next Generation Products**. We firmly believe that OceanBench can help facilitate the design of experiments that can help build the next generation of assimilation and forecasts products.
Using the analogy put forth in [previous sections ](../framework/tasks.md), we see that most problems can be broken down into an interpolation and extrapolation problem.
We can experiment with these components independently to gain insight into the potential of ML.
However, eventually, we need have a coupled system where we can reuse the independent components to develop end-to-end solutions.


---
## Tasks

There are a number of objectives that we can envision that can be implemented with OceanBench.
Ultimately, we are interested in tasks that pertain to the Mercato space.
This boils down to two main tasks: 1) **Interpolation** and 2) **Forecasting**.
We outline them in more detail below.


---
### Interpolation

```{mermaid}
graph LR
    Interpolator --> Data-Assimilator
    Surrogate-Model --> Data-Assimilator
```

The interpolation task will involving using sparse, gappy observations from different sources to produce a full map that is physically consistent.
Logistically, this will involve aggregating as many observations as possible and then projecting them onto a grid using an interpolator or a surrogate.
From research (**TOCITE**), we know that the best methods will need to use physics-informed decisions. 
The main ways which can involve using specialized data structures and architectures, targeted loss functions, or training on historical simulations.

Interpolation methods can work "out-of-the-box" where minimal tuning is needed.
However, more elaborate methods need to be trained on OSSE experiments using reanalysis data.

---
### Forecasting

```{mermaid}
graph LR
    Surrogate-Model --> Forecasting
```

The forecasting task will involving using currently assimilated data and then predicting a map forward in time.
Logistically, this will involve training a surrogate model that is able to take a map (or sequency of sequential maps), and then predict a specified time step forward in time.
The hope is that this prediction is physically consistent.

To obtain such a model, one would need to train on historical reanalysis which captures the blend between physics and observations. 

---
## Experiment Types


### OSSE Experiments


### OSE Experiments


---
## Code-Base Design

