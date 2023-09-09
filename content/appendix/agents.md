---
title: Learning
subject: Modern 4DVar
subtitle: How we choose how to include information at every step
short_title: Agent-Environment
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


## Decision Making

Human beings are a species that is constantly interacting within our environment, the Earth.
Now this relationship can be roughly characterized as following as a feedback loop.

```{figure} https://pbs.twimg.com/media/Ff35C_baEAMlaOe.jpg
:alt: Agent-Env
:width: 250px
:align: center

Agent's ability to learn and predict within its environment. - [Tweet](https://twitter.com/RichardSSutton/status/1584696809565618176)
```


**Environment**.
This is essentially the Earth; true spatiotemporal state of the system. It is huge, it manifests itself at multiple scales, and it is a complex system.
*Note*: We can go further with this and consider outer space or we can also go smaller and consider a smaller region, e.g. a continent, country or city.

**Agents**. 
This is an object or concept that we highlight as something that interacts within the environment.

**Observations**.
These are finite, approximate descriptions of the environment that we can *measure*.
This is effectively how we describe our environment.
It is difficulty is how we measure and store these approximate descriptions, normally in the form of signals.

**Actions**.
An action is how our agent does something which could affect itself and possibly some portion of the environment.
Any action worth characterizing could potentially change the behaviour or state of our agent wrt the environment.
This is easily the most important part because it has the potential to change our entire trajectory, e.g. our life.

**Feedback Loop**.
Overall, this relationship is a closed-system and operates as a sequential cycle:
* the environment exists
* an agent observes something about the environment
* the agent makes an action
* which has an effect on the agent wrt the environment
* we repeat the cycle with another observation


**Reward**.
The reward is the *prize* that the agent receives from the environment.
It could be something positive or it could be something negative.
It's natural to want to receive all positive rewards or perhaps avoid all negative rewards.


**Decision-Making**
Now, an agent normally has a set of different actions that it can take.
So now, some questions we could ask are:

* *which actions can I take*?
* *which action should I take*?
* *why should I take said action*?

This is decision-making as we 


---
## Intelligence


