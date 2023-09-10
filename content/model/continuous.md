---
title: Continuous Representation
subject: Modern 4DVar
subtitle: How can we model data with a continuous representation?
short_title: Continuous Representation
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
---


# Motivation

In my experience, we seem to jump a little bit when talking about models and data representations, especially in the geosciences. We often jump straight to image-to-image applications without really thinking about the data/functa. I think there is a logical progression that describes data by the means of coordinates, data, and models. This is my interpretation of how we can describe data and its representations and what we hope to achieve. Throughout this entire tutorial, I will be using sea surface height (SSH) as my example quantity of interest to showcase how each of these quantities are related.

### My Objective

I hope that this will bring some cohesion between different concepts in terms of *data* and *modeling*. I also think it will help me as a (future) machine learning research engineer to make some things *more* concrete with different abstractions. I sincerely believe that it will make my research skills better and also my programming skills as I try to tame the wildness. Abstraction and Ontology is very important in SWE and I think it should be important in geosciences. Also, those who know me, always know that I like to understand the *information flow* of peoples ideas and that I will almost always ask what the *shape of the data* is when fed into our machines. I have strong feelings about the *information flow* of systems (more later) but I also think that thinking about data representations in geoscience is really an underrated idea…

### Format

The rest of the blog post will go through some of the fundamental concepts we need for modeling in geoscience. From the data side, we have the *space* that defines the coordinate system and the *domain* which defines the range of values for the coordinates. From the modeling side, we have the *physical model* which defines some constraints in the form differential operators in space and time and we also have *parameterized models* which are functions with learnable parameters. Lastly, we come back to reality with observations which can be the same as the data or some other proxy which we believe is related. I end this will some somber news about why these abstracts are only the containers because the real world we live in really limit our ability to learn models based on data.

---

# Space

Almost no quantity of interest (QOI) exist within a vacuum. We almost always assume that our quantities of interest lie within some spatial-temporal space, even if we choose to ignore it. For example, they may spatially lie within a pixel space (e.g. an image) and temporally lie along a time line. In most geoscience applications, we can define some arbitrary coordinate system which varies in space and time. Let


$$
\mathbf{x}_s \in \mathbb{R}^{D_s}, \hspace{5mm} t \in\mathbb{R}^+
$$ (functa_space)

where $\mathbb{R}^{D_s},\mathbb{R}^{+}$ is the domain for all possible queries in space and time. It represents the form of the queries for each of these QOIs. The full domain $\mathbb{R}$ represent the infinite values that the coordinates can have and the exponent defines the properties of the coordinate. In general, a single spatial coordinate is a vector of size $D_s$ and a single temporal coordinate is a positive integer. These coordinates define the entire space where “data” can lie.  For example, we can have the Cartesian coordinate system which is generally rectangular, cubic or hyper-cubic. We could also have the spherical coordinate system which is circular, spherical or hyper-spherical. We can also have some hybrid version of the two, e.g. the cylindrical coordinate system, or some other very funky coordinate systems.

````{admonition} Code Formulation
:class: dropdown idea

One example of a space

```python
x_domain: obj = Space("euclidean")
```

Perhaps we could sample from this domain

```python
x_samples: Array["100"] = x_domain.sample(100)
```

Now the minimum and maximum of these samples would be between $(-\infty,\infty)$.

````

````{admonition} Example: Sea Surface Height
:class: dropdown info

My application is geoscience so everything lives on the Earths core, surface or atmosphere.

````

````{admonition} Better Discussion
:class: dropdown seealso

For more details on the notion of spaces and coordinates, please see [this jbook](https://r-spatial.org/book/02-Spaces.html) where they have a detailed discussion about coordinate reference systems. It is the jupyter-book of the full book: [Spatial Data Science with Applications in R](https://www.routledge.com/Spatial-Data-Science-With-Applications-in-R/Pebesma-Bivand/p/book/9781138311183).

````




---

# Domain

In almost all cases in geoscience, we can take the Earth as the domain where all the geophysical quantities lie. If we were to think about Cartesian coordinate system and the Earth, we could assume that the center of the earth is the origin of the domain and the values are bounded between 0 and the radius of the Earth, e.g. ~6,371 km (perhaps a bit further into space if we account for the atmosphere). We can also think about it in spherical terms which bounds the domain in terms of how many rotations, e.g. $-2\pi,2\pi$. We can even be interested in subregions along the globe like the Mediterranean sea or the open ocean. For the spatial domain, we define $\Omega$ as proper subset of the entire domain $\mathbb{R}^{D_s}$. For the temporal domain, $\mathcal{T}$, it is usually defined along a bounded number line $\mathcal{T}\in[0, T]$. However, we could also use the 24 hour clock as well as cyclic calendars with years, months and days. So more concretely, we define our coordinate system where our quantities of interest lie as

$$
\mathbf{x}_s \in \Omega \subset \mathbb{R}^{D_s}, \hspace{5mm} t\in\mathcal{T}\subset\mathbb{R}^+
$$ (functa_domain)

There are of course simplifications to this system. For example, we could be looking for processes that stationary (don’t change in time) or constant (don’t change in space). However, both are sub-cases and are still covered within this notation!





---

# Functa (Data)




---



### Non-Parametric Models

- **Example: Regression**


    Which functions do we use will depend upon the data representation, the assumptions of the solutions, the computational power we have, the amount of datapoints we have, and any additional constraints. We can use neural fields (NerFs) which are coordinate-based neural networks. We can also use Gaussian processes (GPs) which are non-parametric, probabilistic, functional methods.

