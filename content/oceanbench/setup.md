---
title: Experimental Setup
subject: Modern 4DVar
subtitle: The datasets available for training ML methods.
short_title: Setup
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


```{mermaid}
graph LR
    Obs-Data --> ML-Ready-Data
    Sim-Data --> ML-Ready-Data
    ML-Ready-Data --> ML-Ideation
    ML-Ideation --> ML-Ideation
    ML-Ideation --> ML-Tool
    ML-Tool --> MLOPs
    ML-Tool --> Research
    ML-Tool --> Evaluation
    MLOPs --> Product
```