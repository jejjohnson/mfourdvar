---
title: Geometry
subject: Modern 4DVar
subtitle: What do we actually want?
short_title: Geometry
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


> This section introduces the concepts of spaces, coordinates and domains.


**TLDR**

$$
\begin{aligned}
\text{Spatial}: && &&
\vec{\mathbf{x}} &\in \boldsymbol{\Omega} 
\subseteq \mathbb{R}^{D_s} \\
\text{Tempoeral}: && &&
t &\in \boldsymbol{\mathcal{T}} 
\subseteq\mathbb{R}^+ \\
\end{aligned}
$$


**Motivating Examples**:
* `xarray.Dataset` - coordinates & Values - [Documentation](https://docs.xarray.dev/en/latest/user-guide/data-structures.html)
* `geopandas.GeoSeries` -  - [Documentation](https://geopandas.org/en/stable/docs/user_guide/data_structures.html)
* `rasterio` - Polygons, Rasters

---
### Spaces 


$$
\begin{aligned}
\text{Spatial}: && && &\mathbb{R}^{D_s} \\
\text{Tempoeral}: && && &\mathbb{R}^+ \\
\end{aligned}
$$

* Lines - Temporal Plane
* Cartesian - Spatial Plane
* Spherical - Global
* Infinite...

```python
space: Space = Line()
space: Space = Cartesian()
space: Space = Spherical()
```


**Examples**:
* [torchphysics](https://torchphysics.readthedocs.io/en/latest/api/torchphysics.problem.spaces.html)
* [phiflow](https://tum-pbs.github.io/PhiFlow/phi/geom/index.html)


---
**Example: Time Series**


---
**Example: Gulfstream**


---
**Example: Earth**


---
### Domains

In almost all cases in geoscience, we can take the Earth as the domain where all the geophysical quantities lie. If we were to think about Cartesian coordinate system and the Earth, we could assume that the center of the earth is the origin of the domain and the values are bounded between 0 and the radius of the Earth, e.g. ~6,371 km (perhaps a bit further into space if we account for the atmosphere). We can also think about it in spherical terms which bounds the domain in terms of how many rotations, e.g. $-2\pi,2\pi$. We can even be interested in subregions along the globe like the Mediterranean sea or the open ocean. For the spatial domain, we define $\Omega$ as proper subset of the entire domain $\mathbb{R}^{D_s}$. For the temporal domain, $\mathcal{T}$, it is usually defined along a bounded number line $\mathcal{T}\in[0, T]$. However, we could also use the 24 hour clock as well as cyclic calendars with years, months and days. So more concretely, we define our coordinate system where our quantities of interest lie as

$$
\mathbf{x}_s \in \Omega \subset \mathbb{R}^{D_s}, \hspace{5mm} t\in\mathcal{T}\subset\mathbb{R}^+
$$ (functa_domain)

There are of course simplifications to this system. For example, we could be looking for processes that stationary (don’t change in time) or constant (don’t change in space). However, both are sub-cases and are still covered within this notation!


$$
\begin{aligned}
\text{Spatial Domain}: && &&
\boldsymbol{\Omega} &\subseteq \mathbb{R}^{D_s} \\
\text{Tempoeral}: && &&
\boldsymbol{\mathcal{T}}&\subseteq \mathbb{R}^+ \\
\end{aligned}
$$

**Analogous to Regions & Periods**

---
**Example: `xarray.Dataset`**

```python
# selecting time (GulfStream)
xarray.Dataset.sel(lon=slice(-65, -55), lat=slice(33, 43))
# selecting period (This Year)
xarray.Dataset.sel(time=slice("2023-01", "2023-08"))
```


---
### Coordinates



```python
x, y = space.coords
X, Y = space.grid
```


**Examples**:
* `xarray.Dataset.Coordinates` - [Example](https://docs.xarray.dev/en/latest/generated/xarray.core.coordinates.DataArrayCoordinates.html)
* `sunpy.Coordinates` - [Example](https://docs.sunpy.org/en/stable/reference/coordinates/index.html)

#### Coordinate Reference Systems



---
## Examples



````{admonition} Code Formulation
:class: dropdown idea

One example of a domain on a line

```python
t_min: float = 0.0
t_max: float = 1.0
type: str = "line"
time_domain: obj = Domain(bounds=(t_min, t_max))
```

Perhaps we could sample from this domain (infinitely)

```python
samples: Array["inf"] = time_domain.sample(inf)
```

Now the minimum and maximum of these samples would be between $[0,1.0]$. This would be nearly equivalent with a vector of spatial coordinates along a line.

**2D Space Domain**

So let's assume we have a 2D domain that's defined on Euclidean space.

```python
x_space: object = Domain((x_min, x_max))
y_space: object = Domain((y_min, y_max))
```

Now we want to create an object

```python
xy_domain: object = Domain((x_domain, y_domain))
```

````


````{admonition} Example: Sea Surface Height
:class: dropdown note

For sea surface height, it can exist on the surface of a sphere (roughly). This has the spatial coordinates as latitude, longitude and we can set some arbitrary temporal some coordinates as days.

$$
\mathbf{x}_s = [\text{latitude},\text{longitude}], \hspace{5mm} t=[0 \text{ day},1 \text{ day}]
$$

We can also transform these coordinates into an x,y plane with a higher frequency. For example, we can use the local tangent coordinate system defined over the Gulfstream where SSH is queried every hour.

$$
\mathbf{x}_s=[x,y], \hspace{5mm} t=[\text{hours}]
$$

This is typically what we do in numerical schemes as it can be quite difficult to march along the entire globe, especially at finer resolutions (see my discussion on discretization).

````