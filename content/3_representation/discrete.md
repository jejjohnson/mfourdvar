---
title: Discrete Representation
subject: Modern 4DVar
subtitle: How can we model data with a discrete representation?
short_title: Discretized Representation
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


# Temporal Discretization

We look at the temporal coordinates

$$
t \in \mathcal{T} \subseteq \mathbb{R}^{D_t}
$$

A simple example would be to have some time units ranging from zero to some constant like

$$
\mathcal{T}=[0, T]
$$

however, we can have other ways of encoding time depending upon the situation. See the *encodings* section below.




# Spatial Discretization



$$
\vec{\mathbf{x}} \in \boldsymbol{\Omega} \subseteq \mathbb{R}^{D_s}
$$

$$
\boldsymbol{\Omega}:=\boldsymbol{\Omega}(t)
$$

# Between Spaces

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

# Encodings


Time can be difficult to encode into a neural network as there are some variables that are cyclic by nature. For example, hours, months, and days of the year are on a cycle. Seasons can also be on a cycle. One option would be to remove these trends from the 

However, we can have some more sophisticated encodings like sinusoidal encodings to encode cyclic features, e.g.

$$
\text{Encoder}(t) =
\left[
\sin\left(\frac{2\pi t}{T}\right), 
\cos\left(\frac{2\pi t}{T}\right)
\right]^\top
$$

or we can do some more sophisticated encoders like sinusoidal embeddings.


# Field Discretization

So we talked about spatial discretization and temporal discretization. However, there is one more discretization concept which might not be obvious at first but it is a fundamental - we can discretize the field itself.


In machine learning, the most obvious example one could think of a pixels within images. The actual pixel value itself can have a value between 0-255. So this is not a continuous representation of values, they are inherently discrete.

Another common problem we choose to solve is one of segmentation.

Lastly, we do the same for classification.

This is very prevalent in applications that require decision-making. We often see extreme event indices like drought or heat whereby we mark a range of values with some semantic meaning. For example, we can say that temperatures that are between 20-30 are normal, temperatures between 30-40 are high and temperatures 40+ are considered extreme. We can do the same for droughts, wildfires and even hurricanes. A more extreme example is when we decide to mark a threshold to say when we act or don't act (a binary classification problem).


---
## Demo Code


**Apply Operations**

```python
# initialize the domain
domain: Domain = ...

# initialize the field
fn: Callable = lambda x: ...
u: Field = Discretization(domain, fn)

# apply operator
du_dx = gradient(u)

# apply operator with predefined params
params: Params = DiscretizationParams(...)
u_grad = gradient(u, params)
```


**Discretization** - Finite Difference

```python
class FDParams:

```
