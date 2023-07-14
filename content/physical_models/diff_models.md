---
title: Differentiable Physics Models
subject: Modern 4DVar
subtitle: Can we learn to emulate physical models?
short_title: Differentiable Models
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
    GCM: General Circulation Model
    QG: Quasi-Geostrophic
    SW: Shallow Water
---

```{mermaid}
graph LR
    Observation-Data --> ML-Ready-Data
    Simulation-Data --> ML-Ready-Data
    ML-Ready-Data --> ML-Ideation
    ML-Ideation --> ML-Ideation
    ML-Ideation --> ML-Tool
    ML-Tool --> MLOPs
    ML-Tool --> Research
    ML-Tool --> Evaluation
    MLOPs --> Product
```

## Criteria


**Chaotic**.
The methods need to feature chaotic systems that we see in nature

**Coupled**. 
The methods should be able to allow us to train parameterizations.
This can manifest itself as a missing term within the PDE itself.
It can also manifest itself as a multistate system whereby we only observe one state, e.g., a multilayer PDE.

**2D Spatiotemporal Structure**.

**Scale**.


## Level I 

> - Simple Chaotic ODEs

#### Lorenz 63

$$
\begin{aligned}
\frac{dx}{dt} &= \sigma (y - x) \\
\frac{dy}{dt} &= x (\rho - z) - y \\
\frac{dz}{dt} &= xy - \beta z
\end{aligned}
$$ (eq:lorenz63)


**Good For**:
* Great for prototyping
* Interpretable
* Low Engineering Efforts
* Chaotic Nature

**Bad For**:
* No Spatiotemporal Structure
* Testing High-Dimensional Capabilities
* Testing Scale 
* Parameterizations


---
#### Lorenz 96

$$
\frac{dx}{dt} = (x_{i+1} - x_{i-2})x_{i-1}-x_i+F
$$ (eq:lorenz96)

**Good For**:
* Great for prototyping
* Interpretable
* Low Engineering Efforts
* Chaotic Nature
* 1D Spatiotemporal Structure

**Bad For**:
* 2D Spatiotemporal Structure
* Testing High-Dimensional Capabilities
* Testing Scale 
* Testing Coupled Parameterizations



#### Lorenz 96 (2 Level)

$$
\begin{aligned}
\frac{dx}{dt} &= (x_{i+1} - x_{i-2})x_{i-1}-x_i + F - \frac{h c}{b} \sum_{j}y_j \\
\frac{dy}{dt} &= -b c (y_{j+2} - y_{j-1})y_{j+1}- c y_j  - \frac{h c}{b} x_i 
\end{aligned}
$$ (eq:lorenz96t)


---
## Level II 

> - Simple Ocean PDEs

#### Quasi-Geostrophic Equations

$$
\partial_t q_k + (u_kq_k)_x + (v_kq_k)_y = F_k + D_k
$$ (eq:qg_form_adv)

SSH is linked to the QG equations via the stream function which we can write this as:

$$
\psi = \frac{g}{f_0}\eta
$$ (eq:qg_ssh_streamfunction)

This adds some additional interpretation how the vorticity term can be interpreted when dealing with the SSH over the globe.

$$
q_l = 
\underbrace{\boldsymbol{\nabla}_H \psi_l}_{\text{Dynamical}} +
\underbrace{(\mathbf{A}\psi)_k}_{\text{Thermal}} +
\underbrace{f_k}_{\text{Planetary}}
$$ (eq:qg_ssh_vorticity)

We also have . See [{cite}`10.3934/dcdss.2022058,10.1175/JTECH-D-20-0104.1`] for more information about this term.



---
#### Shallow Water Equations



---

## Level III

>  Simple Stacked Ocean PDEs

> These are PDE's that exhibit the spatiotemporal structures that are closer to what we are accustomed to seeing in the real world.
> These models also allow us to incorporate hidden processes.
> This is done by having *stacked* models from level II which try to model processes that we cannot directly observe from satellite observations.



---
#### Stacked QG

We are going to be using the formulation that is described in the Q-GCM model. The manual can be found [here](). We write the multi-layer QG equations in terms of the vorticity term, $q$, and the stream function term, $\psi$. We consider the stream function and the potential vorticity to be $N_Z$ stacked  isopycnal layers.


$$
\partial_t q_k + (u_kq_k)_x + (v_kq_k)_y = F_k + D_k
$$ (eq:qg_form_adv)

where the $F_k$ and $D_k$ are forcing terms for each layer, $k$.  The vorticity term is defined as

$$
q = 
\frac{1}{f_0} \boldsymbol{\nabla}_H^2\psi -
f_0\mathbf{A}\psi + \beta(y-y_0)+ \tilde{\mathbf{D}}
$$ (eq:qg_vorticity)

where $\tilde{D}$ is the dynamic topography and $\beta$ is the $\beta$-plane approximation. The term that links each of the layers together, $\mathbf{A}$, is a tri-diagonal matrix that can be written as

$$
\mathbf{A} =
\begin{bmatrix}
\frac{1}{H_1 g_1'} & \frac{-1}{H_1 g_2'} & \ldots & \ldots & \ldots  \\
\frac{-1}{H_2 g_1'} & \frac{1}{H_1}\left(\frac{1}{g_1'} + \frac{1}{g_2'} \right) & \frac{-1}{H_2 g_2'} & \ldots & \ldots  \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \frac{-1}{H_{n-1} g_{n-2}'} & \frac{1}{H_{n-1}}\left(\frac{1}{g_{n-2}'} + \frac{1}{g_{n-1}'} \right) & \frac{-1}{H_{n-1} g_{n-2}'}  \\
\ldots & \ldots& \ldots & \frac{-1}{H_n g_{n-1}'} & \frac{1}{H_n g_{n-1}'}   \\
\end{bmatrix}
$$ (eq:qg_A)



#### Stacked SW