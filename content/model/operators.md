---
title: Operators
subject: Modern 4DVar
short_title: Operators
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


In this section, we will break down the

$$
\begin{aligned}
\text{Variable I}: && 
\vec{\boldsymbol{a}} &= \vec{\boldsymbol{a}}(\vec{\mathbf{x}},t), 
&&
\vec{\mathbf{x}}\in\boldsymbol{\Omega}_a\subseteq\mathbb{R}^{D_a},
&&
t\in\boldsymbol{\mathcal{T}}_a\subseteq\mathbb{R}^+
\\
\text{Variable II}: &&
\vec{\boldsymbol{u}} &= \vec{\boldsymbol{u}}(\vec{\mathbf{x}},t), 
&& 
\vec{\mathbf{x}}\in\boldsymbol{\Omega}_u\subseteq\mathbb{R}^{D_u},
&&
t\in\boldsymbol{\mathcal{T}}_a\subseteq\mathbb{R}^+
\end{aligned}
$$


$$
\boldsymbol{T}[\boldsymbol{a}](\vec{\mathbf{x}},t):
\vec{\boldsymbol{a}}(\vec{\mathbf{x}},t) \rightarrow
\vec{\boldsymbol{u}}(\vec{\mathbf{x}},t)
$$



---
### Simple Example


```python
# obtain values
a: Array = ...
u: Array = ...

# initialize params of transformation
params: Params = Params(w=..., b=...)

# initialize transformation
transform: Callable = lambda a, params: a * params.w + params.b

# apply transformation
u_hat: Array = transform(a, params)

# test to ensure it is equal
np.testing.assert_array_equal(u, u_hat)
```

**Problems**:
* What if the domains are different?
* What about spatiotemporal data?

---
**Motivating Examples**

* Forecasting Problem
* Interpolation Problem
* Multimodal Domain Transformation

---
### Domain

$$
\Omega_u = \boldsymbol{T_\theta}\left(\Omega_a\right)
$$

```python
# Domain 1
field_a: Field = Field(values_a, domain_a)
field_u: Field = Field(values_u, domain_u)

# initialize interpolator
a_to_u_f: Callable = FieldInterpolator(field_u.values, field_u.coords)

# apply interpolator
field_a_on_u: Field = a_to_u_f(field_a.values, field_a.coords)
```


---
### Functional


---
### Latent Space

Variable I —> Variable II
`a = Transformer(u)`
`z_u = Encoder(u)`
`z_a = LatentTransformer(z_u)`
`a’ = DecoderD2(z_a)`


**Examples**:
* Lift & Learn
* Koopman Theory
* Neural Operators
