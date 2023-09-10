---
title: Overview
subject: Modern 4DVar
subtitle: What do we actually want?
short_title: Overview
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


# Motivation

In my experience, we seem to jump a little bit when talking about models and data representations, especially in the geosciences. We often jump straight to image-to-image applications without really thinking about the data/functa. I think there is a logical progression that describes data by the means of coordinates, data, and models. This is my interpretation of how we can describe data and its representations and what we hope to achieve. Throughout this entire tutorial, I will be using sea surface height (SSH) as my example quantity of interest to showcase how each of these quantities are related.

### My Objective

I hope that this will bring some cohesion between different concepts in terms of *data* and *modeling*. I also think it will help me as a (future) machine learning research engineer to make some things *more* concrete with different abstractions. I sincerely believe that it will make my research skills better and also my programming skills as I try to tame the wildness. Abstraction and Ontology is very important in SWE and I think it should be important in geosciences. Also, those who know me, always know that I like to understand the *information flow* of peoples ideas and that I will almost always ask what the *shape of the data* is when fed into our machines. I have strong feelings about the *information flow* of systems (more later) but I also think that thinking about data representations in geoscience is really an underrated idea…

### Format

The rest of the blog post will go through some of the fundamental concepts we need for modeling in geoscience. From the data side, we have the *space* that defines the coordinate system and the *domain* which defines the range of values for the coordinates. From the modeling side, we have the *physical model* which defines some constraints in the form differential operators in space and time and we also have *parameterized models* which are functions with learnable parameters. Lastly, we come back to reality with observations which can be the same as the data or some other proxy which we believe is related. I end this will some somber news about why these abstracts are only the containers because the real world we live in really limit our ability to learn models based on data.
