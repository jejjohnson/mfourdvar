---
title: Geoscience Data Structures
subject: Modern 4DVar
subtitle: What do we actually want?
short_title: Geoscience
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
    PI: Principle Investigator
---




> All-inclusive


---
### Raster Data

> Raster data is **any pixelated (or gridded) data where each pixel is associated with a specific geographical location**. The value of a pixel can be continuous (e.g. elevation) or categorical (e.g. land use). If this sounds familiar, it is because this data structure is very common: it's how we represent any digital image. - [Data Carpentry](https://datacarpentry.org/organization-geospatial/01-intro-raster-data#:~:text=Raster%20data%20is%20any%20pixelated,we%20represent%20any%20digital%20image.)

#### Discrete

* GeoTiff
* Rasterio


#### Continuous

* xarray
* array
* dataframe

---
### Vector Data

> Vector data structures represent specific features on the Earth’s surface, and assign attributes to those features. Vectors are composed of discrete geometric locations (x, y values) known as vertices that define the shape of the spatial object. The organization of the vertices determines the type of vector that we are working with: point, line or polygon. - [Data Carpentry](https://datacarpentry.org/organization-geospatial/02-intro-vector-data.html)


#### Points


#### Lines


#### Polygons


---
### Key Differences


