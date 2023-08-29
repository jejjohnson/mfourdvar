---
title: Literature
subject: Modern 4DVar
subtitle: Some Literature that might be useful
short_title: Literature
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




---
## Research Questions

> This is inspired by the talk by [Steve Penny](https://events.ecmwf.int/event/304/timetable/) - [Recording](https://vimeo.com/770758490/bac45588aa) | [Slides](https://events.ecmwf.int/event/304/contributions/3615/attachments/2139/3786/ECMWF-ESA-ML_Penny.pdf)

### Reanalysis vs Simulations vs Observations

> Observations and Reanalysis are inherently imperfect data sources with often uncharacterized uncertainties.

* Q1: Are reanalysis datasets an adequate source of training data for ML?
* Q2: Are pure simulation datasets more effective data for ML?
* Q3: How will biases & systematic errors be handled?
* Q4: Can we learn directly from observations plus basic physics constraints?

**Reanalysis-Based**

**Simulation-Based**

**PINNS in the Wild**

[{cite}`10.1088/1748-9326/ac38d9`]

### Hybrid Models

> As numerical Forecasts are modernized (e.g. written in new languages that support differentiation, and designed to take advantage of GPUs), can AI/ML solutions maintain a competitive edge (in terms of computational cost) over conventional modeling.

[{cite}`10.5194/gmd-14-7425-2021,10.48550/arXiv.2207.00556,10.48550/arXiv.2102.11192,10.1073/pnas.2101784118`]

### Model Error Estimation

> How much State Dependent (Conventional) Model error can we learn from comparison with observations?
> How do we separate system observation errors from systematic model forecast errors?

[{cite}`10.48550/arXiv.2209.11510,10.1029/2022MS003016,10.1063/1.5028373,10.1029/2021MS002712`]


### Subgrid Parameterization

> This is an instance of

[{cite}`10.1029/2022MS003124`]

### Better Metrics

> 

[{cite}`10.1103/PhysRevFluids.6.024607`]



---
## Operational Center

### Observation Datasets

**AlongTack**

* {cite}`10.48670/moi-00147`

**In-Situ**

* Currents - {cite}`10.48670/moi-00041`
* Stuff - {cite}`10.48670/moi-00036`
* ARGO - {cite}`10.3389/fmars.2020.00700,10.17882/42182`


### Extrapolation Datasets

**Forecast**

* OceanPhysics - {cite}`10.48670/moi-00016` | Ensemble - {cite}`10.48670/moi-00024`
* Ocean Biogeochemistry - {cite}`10.48670/moi-00015`
* Ocean Waves - {cite}`10.48670/moi-00017`


**HindCast**

### Reanalysis Datasets

* {cite}`10.48670/moi-00021`
* CDS - {cite}`10.24381/cds.67e8eeb7` | SST - {cite}`10.24381/cds.ab205634`
* NCEP - {cite}`10.1175/1520-0493(1998)126<1013:AICMFE>2.0.CO;2`
* NCI - {cite}`10.1016/j.ocemod.2021.101849,10.5194/essd-13-5663-2021`
* [List of Data](https://psl.noaa.gov/data/oceanwrit/datasets/)


---
## Applications

### Plants n Things

* Hanna Meyer - [Slides](https://events.ecmwf.int/event/304/contributions/3621/attachments/2145/3795/ECMWF-ESA-ML_Meyer.pdf) | [Videos](https://vimeo.com/770843010/5350ca5d4e)
* Nature Conservation - {cite}`10.1038/s41467-022-27980-y`
* Agriculture


### Water n Things

* Maritime Risk Predictions - {cite}`10.1080/03088839.2023.2209788,10.1080/01441647.2022.2036864`
* IoT - [example](https://www.iotforall.com/iot-use-cases-in-ocean-conservation)
* Monitoring Ocean Health - {cite}`10.3389/fmars.2017.00020,10.1016/j.oneear.2020.05.013`
* Underwater Exploration and Ocean Cleanup
* Sustainable Fishing Practices
* Marine Protected Areas
* Ocean Energy Solutions



---
# Data Assimilation


## Algorithms


### Back-and-Forth Nudging

* {cite}`10.1088/1742-6596/135/1/012011,10.1051/cocv/2011004`