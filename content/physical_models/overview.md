---
title: Overview
subject: Modern 4DVar
subtitle: Can we learn to emulate physical models from simulations?
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
    GCM: General Circulation Model
    QG: Quasi-Geostrophic
    SW: Shallow Water
---

```{mermaid}
graph TD
    Interpolators --> Variational-Solver
    Differentiable-Models --> Variational-Solver
    Surrogate-Models --> Variational-Solver
```