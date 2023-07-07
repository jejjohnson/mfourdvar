---
title: Physics Informed
subject: Modern 4DVar
subtitle: How we can add physics into our models
short_title: Physics-Informed
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


![Image](https://media.springernature.com/lw703/springer-static/image/art%3A10.1038%2Fs42254-021-00314-5/MediaObjects/42254_2021_314_Figb_HTML.png)

There are many opportunities to add physics-informed information into these systems.



---
# Data

> This is the easiest but not necessarily the most obvious way to 


## Transfer Learning

## Plug-in-Play Priors


---
# State Representation + Architecture

* Encoding:
    * Regularity, e.g. RK4
    * Symmetries, e.g. equivariant, invariant
    * Conservation Laws, e.g. conservation of mass, energy, rotational invariance
* Operator Learning
* Universal Differential Equations
    * incorporating NN into traditional PDE solvers

## NerFs + Siren


## Finite Difference + CNNs


## Euler + ResNets


---
# Loss


## PINNS

Add governing equations to the loss function.


## NerFs + PINNs

## CNNs + LSTMs + PINNS
