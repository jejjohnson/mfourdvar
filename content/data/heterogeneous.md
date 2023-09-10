---
title: Heterogeneous
subject: Modern 4DVar
subtitle: What do we actually want?
short_title: Heterogeneous
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



**Motivating Examples**:
* Raster
* Raster & Vector


---
## Domain Transformation



Variable I - Encoder-Decoder
`z_u = EncoderD1(u)`
`u’ = DecoderD1(z_u)`

Variable II - Encoder-Decoder
`z_a = EncoderD2(a)`
`a’ = DecoderD2(z_a)`

### Between Spaces

In many cases, we are not operating on the same spatiotemporal domain. This is often the case when we are dealing with observations.

### Case I: Same Time, Same Space

$$
\begin{aligned}
\boldsymbol{\Omega}_z &= \boldsymbol{\Omega}_u \\
t_z &= t_u
\end{aligned}
$$

This is the common framework for simulated data.

### Case II: Same Time, Differnt Space

$$
\begin{aligned}
\boldsymbol{\Omega}_z &\neq \boldsymbol{\Omega}_u \\
t_z &= t_u
\end{aligned}
$$

This is the common problem for interpolation and extrapolation problems.


### Case III: Different Time, Different Space


$$
\begin{aligned}
\boldsymbol{\Omega}_z &\neq \boldsymbol{\Omega}_u \\
t_z &\neq t_u
\end{aligned}
$$

This is common for forecasting problems whereby we have a latent space that  we are confident in but the QOI of interest that we want to predict lies in a different spatiotemporal domain.




---
**Example: (Un)structured to (Un)Structured Grids**


```python
# Field 1
values: Array = ...
domain: Domain = ...
u: Field = Field(values, domain)

# define new domain
new_domain: Domain = ...

# interpolation (functional API)
interp_fn: Callable = Interpolator(new_domain)

# interpolate onto new grid
u_new: Field = interp_fn(u.values, u.domain)
```

More information about some grid interpolation schemes can be found for [`scipy.interpolate`](https://docs.scipy.org/doc/scipy/tutorial/interpolate.html), [`pyinterp`](https://pangeo-pyinterp.readthedocs.io) , [`xesmf`](https://xesmf.readthedocs.io/en/stable/) and [`xarray`](https://docs.xarray.dev/en/latest/user-guide/interpolation.html) has some native interpolation schemes.

---
**Example: Finite Volume Grids**


---
**Example: Earth Science Data Cubes (ESDC)**

Often times, people (including me, a ML researcher) do not want to have to deal with many of these problems of domainThese are data structures


**Resources**:
* Deep Earth System Data Lab (DeepESDL) - [Website](https://www.earthsystemdatalab.net) | [Paper](https://esd.copernicus.org/articles/11/201/2020/)
* [xcube](https://xcube.readthedocs.io/en/latest/) 
* [OpenData Cube](https://www.opendatacube.org)




