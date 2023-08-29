---
title: Optimization
subject: Modern 4DVar
subtitle: How do we find the best solution to our problem?
short_title: Optimization
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


# 1st Order Optimization

These are very common optimizers like SGD, Adam or AdamW.


# 2nd Order Optimization

These are less common optimizers but these typically converge much faster than 1st order methods. 
Most of these stem from the Gauss-Newton approximation method.
However, the naive approach is often too expensive.

* Low Rank Approximations - BFGS, L-BFGS
* Iterative Methods - Hessian-Free Optimization
* Structured Approximations - K-FAC methods


# Gauss-Newton Dual Form

There is some recent work that tries to generalize these higher-order schemes under a single umbrella.
They call it the Gauss-Newton dual criteria [{cite}`10.48550/arXiv.2308.08886`]