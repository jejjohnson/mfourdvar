---
title: Sea Surface Height Interpolation Edition
subject: Modern 4DVar
subtitle: How can we fill in the gaps from Sea Surface Height Observations
short_title: SSH Interpolation
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

This is the first edition of the OceanBench framework.


```{mermaid}
graph LR
    Observation-Data --> ML-Ready-Data
    Simulation-Data --> ML-Ready-Data
    ML-Ready-Data --> ML-Ideation
    ML-Ideation --> ML-Ideation
    ML-Ideation --> ML-Tool
    ML-Tool --> MLOPs
    ML-Tool --> Research
    ML-Tool --> Evaluation
    MLOPs --> Product
```

## Data Challenges

We us the OSSE and OSE framework for SSH interpolation.


### OSSE Experiments

Each subsequent experiment adds more data that is available to the user for usage in their algorithms.
However, it is encouraged to use ablations to see which of the datasets had the most impact on the learning scheme.

```{mermaid}
graph TD
    OSSE-NADIR --> ML-Ready-Data
    OSSE-SWOT --> ML-Ready-Data
    OSSE-SST --> ML-Ready-Data
```


#### I - OSSE NADIR

We use satellite-based [NADIR altimetry tracks](https://ggos.org/wp-content/uploads/2021/10/obs_satellite_altimetry_ggos_web_v2-1024x805.png). 
The original simulation stems from a high-resolution ocean simulation stemming from the NEMO model [{cite}`10.1029/2019JC015827`].

#### II - OSSE SWOT

This experiment uses both the NADIR and SWOT altimetry data.
The SWOT satellite offers a higher spatial resolution but a lower temporal resolution.
In principal, this would allow us to see more detail in the spatial structures [{cite}`10.1175/JTECH-D-15-0160.1`].
However, this offers more challenges because the amount of data captured from the SWOT simulator is much, much higher than that of the NADIR altimeters.


#### III - OSSE NADIR + SWOT + SST

This experiments adds the use available SST data to aid in training.
From a *scientific* perspective, there are deep connections between SSH and SST as they are often jointly estimated in large Ocean GCMs  [{cite}`10.1029/2019JC015827`].
From a *practical* perspective, SST is more abundant in operational settings, at higher resolutions and often with less gaps.

### OSE Experiments


```{mermaid}
graph TD
    OSE-NADIR --> ML-Ready-Data
```
