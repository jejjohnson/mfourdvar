---
title: BiLevel Estimation
subject: Modern 4DVar
subtitle: How can I estimate the state AND the parameters?
short_title: Bi-Level Estimation
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

> In these examples, we will


$$
\begin{aligned}
\boldsymbol{\theta}^* &= 
\underset{\boldsymbol{\theta}}{\text{argmin}}
\hspace{2mm}
\boldsymbol{L}(\boldsymbol{\theta})\\
\boldsymbol{x}^*(\boldsymbol{\theta}) &=
\underset{\boldsymbol{\theta}}{\text{argmin}}
\hspace{2mm}
\boldsymbol{J}(\boldsymbol{x};\boldsymbol{\theta}) 
\end{aligned}
$$