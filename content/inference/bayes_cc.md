---
title: Bayesian Crash Course
subject: Modern 4DVar
subtitle: Bayesian Interpretation of all Problems
short_title: Bayes For Inference/Learning
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

This document goes over the Bayesian formulation in relation to some of the estimation and learning problems we have identified earlier.

* State and Observations
* Parameters and Data
* State, Parameters & Data
* Temporal State and Observations
* Temporal State, Parameters & Data


## State & Observations

In this case, we are interested in


**Joint Distribution**

$$
p(\boldsymbol{z},\boldsymbol{y}) =
p(\boldsymbol{y}|\boldsymbol{z})p(\boldsymbol{z}) =
p(\boldsymbol{z}|\boldsymbol{y})p(\boldsymbol{y})
$$

**Posterior**

$$
p(\boldsymbol{z}|\boldsymbol{y}) =
\frac{p(\boldsymbol{y}|\boldsymbol{z})p(\boldsymbol{z})}{p(\boldsymbol{y})}
$$

**Evidence**

$$
p(\boldsymbol{y}) =
\int p(\boldsymbol{y}|\boldsymbol{z})p(\boldsymbol{z}) d\boldsymbol{z}
$$

**Posterior Predictive Distribution**

$$
p(\boldsymbol{u}|\boldsymbol{z}) =
\int p(\boldsymbol{u}|\boldsymbol{z})
p(\boldsymbol{z}|\boldsymbol{y})
d\boldsymbol{z}
$$

---

## Parameters & Data


Given some data $\mathcal{D} = \left\{ u_n, z_n\right\}_{n=1}^N$

**Joint Distribution**

$$
p(\boldsymbol{\theta},\mathcal{D}) =
p(\boldsymbol{\theta}|\mathcal{D})
p(\mathcal{D}) =
p(\mathcal{D}|\boldsymbol{\theta})
p(\boldsymbol{\theta})
$$

**Posterior**

$$
p(\boldsymbol{\theta}|\mathcal{D}) =
\frac{p(\mathcal{D}|\boldsymbol{\theta})}{p(\mathcal{D}) }
$$

**Evidence**

$$
p(\mathcal{D}) = 
\int p(\mathcal{D}|\boldsymbol{\theta})
p(\boldsymbol{\theta})
d\boldsymbol{\theta}
$$

**Posterior Predictive Distribution**

$$
p(\boldsymbol{u}|\boldsymbol{z},\boldsymbol{\theta}) =
\int p(\boldsymbol{u}|\boldsymbol{z},\boldsymbol{\theta})
p(\boldsymbol{\theta}|\mathcal{D})
d\boldsymbol{\theta}
$$

---

## State, Parameters & Data

**Joint Distribution**

$$
p(\boldsymbol{z},\boldsymbol{\theta},\boldsymbol{y}) =
p(\boldsymbol{z}|\boldsymbol{y},\boldsymbol{\theta})
p(\boldsymbol{y}) =
p(\boldsymbol{y}|\boldsymbol{z},\boldsymbol{\theta})
p(\boldsymbol{z}|\boldsymbol{\theta})
p(\boldsymbol{\theta})
$$

**Posterior**

$$
p(\boldsymbol{z}|\boldsymbol{\theta}|\boldsymbol{y}) =
\frac{1}{Z}
p(\boldsymbol{z}|\boldsymbol{z},\boldsymbol{\theta})
p(\boldsymbol{z}|\boldsymbol{\theta})
p(\boldsymbol{\theta})
$$

**Evidence**

$$
\mathbf{Z} =
\int p(\boldsymbol{y}|\boldsymbol{z},\boldsymbol{\theta})
p(\boldsymbol{z}|\boldsymbol{\theta})
p(\boldsymbol{\theta})
d\boldsymbol{\theta}
$$

**Posterior Predictive Distribution**

$$
p(\boldsymbol{u}|\boldsymbol{z},\boldsymbol{\theta}) =
\int p(\boldsymbol{u}|\boldsymbol{z},\boldsymbol{\theta})
p(\boldsymbol{z}|\boldsymbol{\theta}|\boldsymbol{y})
d\boldsymbol{z}
$$