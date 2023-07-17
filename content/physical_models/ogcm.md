---
title: Ocean General Circulation Models
subject: Modern 4DVar
subtitle: Can we learn to emulate physical models from simulations?
short_title: Ocean GCMs
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
    GCM: General Circulation Model
    QG: Quasi-Geostrophic
    SW: Shallow Water
---

There are many sophisticated Ocean GCM's that exist within the community like NEMO and MOM6.
However, these are very complex systems with many internal parts and parameterizations.
There have been some attempts to convert some of these mega systems into differentiable models [{cite}`10.5194/gmd-11-3299-2018`] or rebuild them from scratch [{cite}`10.21105/joss.02018`].
However, it would undeniably be a huge effort to convert all of these systems into differentiable models.
In addition, it might not be useful to have such a large differentiable system because the back-propagation process throughout the entire system in a learning-based setting might not be feasible.

A different approach is to train surrogate models to emulate individual components of the system.