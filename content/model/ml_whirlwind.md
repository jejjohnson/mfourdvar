---
title: Machine Learning Whirlwind Tour
subject: Modern 4DVar
short_title: Parameterized Model
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
---


```{list-table} This table showcases a few ways to parameterize a model.
:header-rows: 1
:name: tb:model-architecture-whirlwind

* - Parameterization
  - Equation
* - Linear
  - $\mathbf{Wx} + \mathbf{b}$
* - Basis Function
  - $\mathbf{W}\boldsymbol{\phi}(\mathbf{x})+\mathbf{b}$
* - Non-Linear Function
  - $\sigma\left(\mathbf{Wx}+\mathbf{b}\right)$
* - Neural Network
  - $\sigma\left(\mathbf{Wx}+\mathbf{b}\right)$
* - Functional
  - $p(\boldsymbol{f}(\cdot))\sim \mathcal{GP}$
```