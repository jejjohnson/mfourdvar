---
title: Marine Data Store
subject: Modern 4DVar
subtitle: The datasets available for training ML methods.
short_title: Data
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
    MDS: Marine Data Store
---


The [Marine Data Store (MDS)](https://data.marine.copernicus.eu/products) has a lot of data that is available that can be used for training an end-to-end ML system.
They have raw observations that come from satellite altimeters and in-situ sources.
There is also a reanalysis product that combines the observations and NEMO model. 
Furthermore they have make forecasts which can be a 'free-run' product.
All of the data listed here are available from the Copernicus project via the [MDS](https://data.marine.copernicus.eu/product/GLOBAL_REANALYSIS_PHY_001_031/description).

```{mermaid}
graph TD
    Satellite-Altimetry --> Observations
    In-Situ --> Observations
    GLORYS --> Reanalysis
    NEMO --> Free-Run
```

In this document, we focus on each of the individual components: 1) observations, 2) reanalysis and 3) free-run.
In the remainder of the document, we discuss how we can get access to data for each of the components.



---
## Observation Data

```{mermaid}
graph TD
    Satellite-Altimetry --> Observations
    In-Situ --> Observations
```

There is a number of available observation data available from the platform.
They primarily come in two forms: 1) observations from satellite altimetry and 2) observation from in-situ measurements.

| Name | Type | Variables | Dates | Link |
|:-----|:-----|:---------------------|:------|:------|
| | Satellite Altimetry | SSH | | [Marine Data Store](https://data.marine.copernicus.eu/product/SEALEVEL_GLO_PHY_L3_MY_008_062/description) | |
| | In-Situ | SSH, SST | | [Marine Data Store](https://data.marine.copernicus.eu/product/INSITU_GLO_PHYBGCWAV_DISCRETE_MYNRT_013_030/description)|
| | | SST | | [EUMETSAT](https://www.eumetsat.int/sea-surface-temperature-services) |
| | | SST | | [NASA](https://earthobservatory.nasa.gov/global-maps/MYD28M) |

**Satellite Altimetry**.
The satellite altimetry data is an aggregate from all available satellite altimeters [{cite}`10.48670/moi-00146`].
This is a L3 product that originally comes from the CLS group that use it to create interpolated maps using covariance-based schemes.
It has also been further post-processed to be compatible with the data assimilation schemes used by Mercato.
This has an update frequency of 2hours every day.

**In-Situ Observations**.
The Global Ocean In-Situ database is an aggregate of all available near-real-time observations [{cite}`https://doi.org/10.48670/moi-00036`].
This is a L2 product that originally comes from the IFremer group.
It has also been further processed to be compatible with the data assimilation schemes used by Mercato.
This has an update frequency of daily.



---
## Reanalysis Data

```{mermaid}
graph TD
    GLORYS --> Reanalysis
```

**Global Dataset.**
The GLORYS12V1 [{cite}`10.48670/moi-00021`] product is the CMEMS global ocean eddy-resolving reanalsyis of the alimetry data outlined above. 
It has a horizontal resolution of $1/12^\circ$ and a vertical resolution of 50 levels.
It has assimilated alongtrack alimetry data, satellite sea surface temperature, sea ice concentration and in-situ temperature and salinity vertical profiles.



| Name | Horizontal Resolution | Vertical Levels | Dates | Link |
|:----|:---------------------|:---------------|:------|:---:|
| GLORYS12V1 | $1/12^\circ$ | 50 | 1993 - 2020 | |
| Ensemble | $1/4^\circ$ | 75 | 1993-2020 | [MDS](https://data.marine.copernicus.eu/product/GLOBAL_REANALYSIS_PHY_001_031/description)

The MDS also features an ensemble product [{cite}`10.48670/moi-00024`] which combines the reanalysis of GLORYSV4 (FR), ORAS5 from ECMWF (GER), GloSea5 from Met Office (UK) and C-GLORSv7 from CMCC (IT)



**Why Reanalysis?** 
Reanalysis produces a comprehensive combination of model and observations. 
It uses the outputs of a numerical GCM that simulates the evolution of the ocean state combined with observations to generate a synthesized estimate of the ocean state. 
For a forecasting problem, one approach is to train a model based on reanalysis data because it is the .
Another approach is to train a model based on model data. 
However, we can postulate that the rea


**GLORYS Product**.  
The GLORYS product has the temperature, salinity, current speed, current direction, sea-level, sea-ice extent, sea-ice concentration, and sea-ice thickness.

---
## Free-Run

```{mermaid}
graph TD
    NEMO --> Free-Run
```


---
## Regions

Attacking the global interpolation problem directly would be very difficult without the experience or resources.
It is better to solve a series of drastically, simpler problems until the full architecture is built.
In addition, one could always use transfer learning to retrain the previously learned methodologies on the new region.


```{mermaid}
graph LR
    GulfStream --> Mediterranean
    Mediterranean --> North-Atlantic
    North-Atlantic --> Global
```

The datasets mentioned above cover the globe at a defined resolution.
However, the CEMS service also focuses on particular regions.

| Regions | Extent |
|:-------|:-------:|
| Global | |
| Baltic Sea | |
| Atlantic-Iberian Biscay Irish Ocean | |
| Mediterranean Sea | |
| Atlantic-European North West Shelf | |
|


---
## Resolutions

The same reasoning applies to the resolutions we should apply the methods.
Attacking the very high resolutions would difficult to handle logistically.
The higher resolutions are high-dimensionally and heavily correlated.
The signal complexity is also much higher yet the amount of iid data is not higher.
So we propose to try and solve the problem at different resolutions ranging in increasing complexity.

```{mermaid}
graph LR
    1/4 --> 1/12
```

The datasets mentioned above cover the globe at both the 1/4 and 1/12 degree resolutions.
However, they have some other resolutions for different regions, e.g. Mediterranean.
Choosing the lowest resolution for the smallest region of interest outlined above would be the easiest problem to tackle logistically.
Again, we can also increase the difficultly in terms of scale and signal complexity by either increasing the resolution of the training data/model or changing the region of interest.

---
## Frequency

We repeat the logic from above but for frequency: attacking the problem at a high frequency would be difficult logistically.
So we can try to apply an assimilation scheme at a lower frequency.

```{mermaid}
graph LR
    Monthly --> Daily
```