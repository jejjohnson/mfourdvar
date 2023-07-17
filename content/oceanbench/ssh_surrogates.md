---
title: Sea Surface Height Surrogate Edition
subject: Modern 4DVar
subtitle: How can we obtain emulators of SSH
short_title: SSH Surrogate
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
    OSE: Observing System Experiments
    OSSE: Observing System Simulation Experiments
    SSH: Sea Surface Height
    SST: Sea Surface Temperature
    SWOT: Surface Water Ocean Topography
    GCM: General Circulation Model
---

```{mermaid}
graph LR
    Simulation-Data --> ML-Ready-Data
    ML-Ready-Data --> ML-Ideation
    ML-Ideation --> ML-Ideation
    ML-Ideation --> ML-Tool
    ML-Tool --> MLOPs
    ML-Tool --> Research
    ML-Tool --> Evaluation
    MLOPs --> Product
```


```{mermaid}
graph LR
    FlowMap --> 1-Hour
    FlowMap --> 6-Hours
    FlowMap --> 12-Hours
    FlowMap --> 24-Hours
```