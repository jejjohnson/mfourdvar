---
title: Learning Problem
subject: Modern 4DVar
subtitle: How to think about modern 4DVar formulations
short_title: Learning
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
## Gradient Learning

```{mermaid}
graph LR
    State-Init --> ...
    ... --> State-Solution
    ... --> ...
```

In many cases, we need to find the best state given the state (and parameters). Most gradient update schemes look like the following where it is fixed.


To find the optimal solution of this problem, we can write it down as:

$$
\boldsymbol{z}^{(k+1)} = \boldsymbol{z}^{(k)} + \boldsymbol{g}_k
$$

where $\boldsymbol{g}_k$ is some result of a generalized gradient operator

$$
[\boldsymbol{g}_k, \boldsymbol{h}_{k+1}] = \boldsymbol{g}(\boldsymbol{\nabla_z}\boldsymbol{J},\boldsymbol{h}_k, k; \boldsymbol{\phi})
$$

where $k$ is the iteration, $\boldsymbol{\phi}$ are the parameters of the gradient operator, and $\boldsymbol{h}$ is the hidden state.

$$
\boldsymbol{L}_g\left(\boldsymbol{\phi} \right)
$$



