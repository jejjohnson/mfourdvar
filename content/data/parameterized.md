---
title: Data (Functa)
subject: Modern 4DVar
subtitle: What do we actually want?
short_title: Parameterized
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

## Formulation

Coordinates alone can be thought of as references (or query points) to an actual quantity of interest, $\boldsymbol{f}\in\mathbb{R}^{D}$, which could be a scalar or a vector. Almost all of these quantities live on some domain. I really like the term *functa* to describe these quantities, i.e. the quantity of interest and its context which includes the set of coordinates, the mapping, and the resulting function value. So the function mapping the coordinates to the variable is give as:

$$
\boldsymbol{f}=\boldsymbol{f}(\mathbf{x}_s,t), \hspace{10mm} \boldsymbol{f}:\Omega\times\mathcal{T}\rightarrow\mathbb{R}^{D}
$$ (functa)

In physics, we typically call this a scalar or vector field which means that each value within this field is a scalar or vector value with an associated spatio-temporal coordinate. These *functa* are continuous as there exists infinitely many spatial-temporal queries we can do which lead to infinitely many values of the functa. The actual functa values could also be infinite. I don’t put any restrictions on the actual functa values themselves. I just say that there is a functa value for the infinitely many coordinates we could query which, by association, would result in infinitely many functa values.

**Note**: I did not include any stochastic term in this formulation but one could easily include this here. I don’t know if there exists any stochasticity in nature and it could just be an artefact of our parameterizations. That’s an open debate I have with myself. In either case, I leave this as an artefact and have included a short discussion below.


```{admonition} Emans Thoughts: Storage
:class: dropdown tip

- it’s cheaper to store the mapping rather than the actual (see functa paper)
- Can do both! - store the coordinates & values, xarray

```


```{admonition} Emans Thoughts: Images vs. Geoscience Data
:class: dropdown tip

Pixels -  `height x width x channels`
Don’t think about it as an image →  think about it as a mapping

Images don’t have to… - live in an isolated space with implied coordinates

Geosciences don’t have the luxury of images (we need the coordinates as well)
- everything lives in a relative space
- Need transformations from one domain to another

===
I often get these requirements from geoscientists to want to encode the physical relationships (i.e. interactions between variables) and global information (i.e. the relative position of the measurement and its effect on the overall structure).

For example, when using ML to map the state from $f_1$ to $f_2$, they often don’t want to give the model the actual global, $(\mathbf{x}_s,t)$, coordinates because they are afraid that the model will memorize the state based on it’s global position. But they want the model to know the global structure of the state when making predictions. To get global structure, you need a relative position (not a global position).

I think this conversation always comes up because our intuition doesn’t fit the standard mathematical model / objects that we use.

Practically speaking, you can do this my normalizing your input coordinates, i.e. $(\mathbf{x}_s, t) \rightarrow (\hat{\mathbf{x}_s}, \hat{t})$.

```




```{admonition} Example: Sea Surface Height
:class: dropdown idea

For SSH, we are interested in the height of the ocean above the mean sea level. We can denote this as:

$$
\text{Sea Surface Height [m]} \hspace{10mm} \eta = \boldsymbol{\eta}(\mathbf{x}_s,t)
$$

So although we typically take the SSH values as “data”, they are actually fields/functa which have an associated coordinate for every SSH value and (as mentioned above), in nature, there are infinitely queries we could use which would result in potentially infinitely many SSH values.

```


This can be useful for a few reasons.

The assumption:
$$
\vec{\boldsymbol{u}} \approx \boldsymbol{f_\theta}
$$



---
### Example: Time Series Regression

Let's say we have a time series. In other words, we are assuming that we have a scalar-valued QoI, $u$, which exists on a number line, $\mathbb{R}^+$.

$$
\begin{aligned}
\boldsymbol{u} &= \boldsymbol{u}(t), 
&&
t \in \mathcal{T} \subseteq \mathbb{R}^+
\end{aligned}
$$
where $\mathcal{T}=[2022,2023]$. This is a single location but we are interested in the time series at this particular location. This could be a point on the globe, e.g. the mediterranean at a bench called Valencia, Spain ($\vec{\mathbf{x}}=[39.483971, -0.320847])$, or perhaps an aggregation of a spatial region defined by some polygon, $\boldsymbol{\Omega}$, i.e. $\mathbb{E}[\boldsymbol{\Omega}]$. Now, let's say we have some measurements, $y$. 

$$
\mathcal{D} = 
\left\{ y_n(t_n)\right\}_{n=1}^N = 
\left\{ t_n, y_n\right\}_{n=1}^N
$$

We assume that they are close to our QoI but not exact due to some unknown amount of noise; for simplicity, we assume some independent Gaussian additive noise.

$$
y_n = u_n + \epsilon_n, \hspace{7mm} \epsilon_n \sim\mathcal{N}(0,\sigma^2)
$$

We don't have access to this QoI, $u$, so we instead define a parameterized function, e.g. a neural network.

$$
y = \boldsymbol{f}(t;\boldsymbol{\theta}) + \epsilon
$$
We assume that we have enough data that we can actually learn the underlying function that interpolates the points and fits the model.

---
### Example: Spatial Regression


Often times we have spatial data which spans a region, i.e. a domain $\boldsymbol{\Omega}$. 



However, this example is much harder to do because spatial data is highly correlated, aka *colinearity*. This is a good thing and a bad thing. The bad thing is that the coordinate values, $\vec{\mathbf{x}}$, used to fit the observations, $y$, are not independent. This is expected because we can assume that points close-enough to each other have very similar values. The good thing is that this assumption of 


We define a kernel function
$$
\begin{aligned}
\boldsymbol{k}(x,y) = \sigma^2\exp\left(-\frac{||x-y||_2^2}{2\ell^2}\right) 
\end{aligned}
$$

See the [spatial modelling example](https://docs.jaxgaussianprocesses.com/examples/spatial/#data-loading) from the GPJax package.

