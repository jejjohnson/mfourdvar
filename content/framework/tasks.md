---
title: Objective-Based Introduction
subject: Modern 4DVar
subtitle: What do we actually want?
short_title: Objectives
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


> This walks through the though process 




## Objective

> “The currency of our current age is authenticity.” - Robert 

**Definition**: A description of the thing you want to achieve.

This needs to be identified in order to ensure everyone understands.

**Decision-Making**. 
This is the action you need take which returns some reward.
The reward could be something like your personal survival or something like make more money.
One could easily have a hierarchy of decisions where we have the general decision we need to make and we can decompose this as a sequence of hierarchical decisions.

**Understanding**.
This is the action you need to take to understand something.
This could be thought of as the 

**Just-Because**.
I think we should give an honourary mention to this objective. 
Often times we do things just because.
I find this quite common with people who may not understand the true objective and perhaps they just have sub-objectives.
You can see this in a lot of students, workers and even (scarily) researchers.


---
## Fundamental Tasks

Let's really narrow this down to geoscience-related tasks. 
When it comes to machine learning, we can identity two tasks: **estimation** and **detection**.

---

### Estimation

These involve prediction tasks which output numerical values, i.e. "continuous".
Often times, these are trying to estimate a variable quantity which can be represented with numerical values, e.g. temperature, height, salinity, etc.

In the ML literature, we can see many instances of these under a different name.
For example:

* Regression
* Image-to-Image (Variable-to-Variable)
* Denoising
* Calibration

---

### Detection

I would argue this is a special case of regression because it uses numeric values that have some semantic meaning, i.e. discrete.
Often times, theses are trying to estimate a more semantic quantity or a discretized quantity that can be represented with discrete values, e.g., eddies, number of people, etc.

Again, in the ML literature, we see many instances of these but under a different name.
For example:

* Classification
* Segmentation
* Anomaly Detection
* Clustering

---

## Estimation Problem Formulation

In general, we can represent the estimation task as some sort of transformation, $\boldsymbol{T}$, as an operators which transforms some predictor vector-valued quantity, $\boldsymbol{a}$, to another vector-valued quantity, $\boldsymbol{u}$, which is what we are actually interested in predicting, i.e., a quantity-of-interest (QoI).

$$
\boldsymbol{T}[\boldsymbol{a};\boldsymbol{\theta}](\vec{\mathbf{x}},t):
\boldsymbol{a}(\vec{\mathbf{x}},t)
\in\boldsymbol{\Omega}_a,\mathcal{T}_a
\subseteq \mathbf{R}^{D_a\times T_a}
\rightarrow
\boldsymbol{u}(\vec{\mathbf{x}},t)
\in\boldsymbol{\Omega}_u,\mathcal{T}_u
\subseteq \mathbf{R}^{D_u\times T_u}
$$


---

## Data Formulation

To actually learn this transformation, $\boldsymbol{T}$, we need data, $\mathcal{D}$. Data is a set or collection of observations.

$$
\mathcal{D} = \left\{ a_n, y_n\right\}_{n=1}^N
$$

In geosciences, the QoI is almost never observed so we collect auxillary observations, $y$.

$$
\mathbf{Y} \approx \mathbf{U}
$$



**Note**: here, I am assuming that the predictor is actually measurable.
We could also make the argument that we may need to collect "measurements" of the 


---

## Learning Problem

So, we have the data and we have our problem formulation.
Now, we almost never know the transformation.
We have to *learn* what is the transformation.

---

### Bayesian Formulation

**Prior**. 
We provide some sort of belief about what the transformation is.
This is called the prior $p(\boldsymbol{T})$.

**Data Likelihood**.
We also provide a causal relationship that our transformation can match the data.
In other words.
This is called the **(data) likelihood**.

**Posterior**.
This is the relationship we are interested in learning, what is probability of the .
This is called the posterior, $p()

Using Bayes Rules, we can write Bayes Theorem, we gives us an elegant way to

$$
p(\boldsymbol{T}|\mathcal{D}) = \frac{p(\mathcal{D}|\boldsymbol{T})p(\boldsymbol{T})}{p(\mathcal{D})}
$$

---

### Bayesian Estimation

Once we have the posterior probability, now we can *use* this model to make predictions about our QoI, $\boldsymbol{u}$.
Once again, we assume that there is a likelihood involved which says, $p(\boldsymbol{u}|\boldsymbol{T})$.
Now, we can use Bayesian Posterior distribution which relates how

$$
p(\boldsymbol{u}|\boldsymbol{T}) = \int p(\boldsymbol{u}|\boldsymbol{T})p(\boldsymbol{T}|\mathcal{D})d\boldsymbol{T}
$$

---
## Problems

Now, it would appear that we have all of the tools necessary to solve our problem: we have an idea about a model, we have the data, and we have a learning platform.
However, their are problems with almost all of the underlying details about

---

### Problems with Data, $\mathcal{D}$

**No Data**. 
This is easily the worst problem we could have: we don't have any data to verify the model we propose.

**Sparse Data (<5%)**.
This is a better problem to have than no data but this is still a serious issue.

**Missing Data**.
We normally classify the missingness as *MCAR*, *MAR*, and *MNAR*.

**High-Dimensional**.
On one hand, this starts getting expensive in terms of computation.
On the other hand, this starts getting difficult to learn with.

**Uncertainty**.
There are often many errors in the measurements we acquire. 
Many times those errors are uncharacterized and unknown.
So if we are able to train the model but there are errors, this is drastically counterproductive.

---

### Problems with Variable Domain, $\boldsymbol{\Omega}$

Most of these problems are the domain where the predictors, observations and QoI lie.


**Outside Spatiotemporal Convex Hull**.

**Inside Spatiotemporal Convex Hull**.

**Irregular Hull Shape**.

---

### Problems with Transformation, $\boldsymbol{T}$


**Unknown Transformation**.


**Incorrect Transformation**.

**Approximate Transformation**.

**Expensive Transformation**.
This can manifest itself within the computation and the memory.

---

### Problems with Learning, $p(\boldsymbol{T}|\mathcal{D})$

**Solution Doesn't Exist**.

**Finding the Solution**.
Can we find the solution and if so, how do we find the solution.

**Solution Found**.
How do we know when we have found the solution?

**Speed to Solution**.
How fast can we find the solution?

**How do we start**?



---
## Common Problems


---
### Interpolation


---
### X-Casting


#### Hindcasting

#### Nowcasting

#### Forecasting

[{cite}`10.1038/s41467-022-32483-x,10.48550/arXiv.2212.12794,10.48550/arXiv.2302.10364`]

* {cite}`10.48550/arXiv.2304.07029`
* {cite}`10.48550/arXiv.2306.05014`








---
## Assimilation

> Using observations to improve our predictions




---
## Decision Making

---
## Digital Twin

> The all inclusive system

