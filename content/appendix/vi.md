 
:::{prf:proof}
:class: dropdown



We want to find the optimal soft predictor by solving the problem of minimizing the population log-loss. 
However, 

$$
q^*(\cdot|\cdot) = 
\underset{q(\cdot|\cdot)}{\text{argmin}} \hspace{2mm}
\mathbb{E}_{(z,y)\sim p(z,y)}
\left[ -\log q(z|y)\right]
$$

Looking at the Bayes theorem, we con deconstruct this population loss as a conditional distribution.

$$
p(z,y) = p(z|y)p(y)
$$

We can use the law of iterated expectations to use this as follows

$$
q^*(\cdot|\cdot) = 
\underset{q(\cdot|\cdot)}{\text{argmin}} \hspace{2mm}
\mathbb{E}_{y\sim p(y)}
\underbrace{
    \left[\mathbb{E}_{z\sim p(z|y)}
\left[ -\log q(z|y)\right]
\right]}_{\text{Cross Entropy}}
$$

We know that the distribution of the observation data doesn't change and we have...
So we can write this in terms of the cross entropy alone

$$
q^*(\cdot|y) = 
\underset{q(\cdot|y)}{\text{argmin}} \hspace{2mm}
\mathbb{E}_{z\sim p(z|y)}
\left[ -\log q(z|y)\right]
$$

which is the cross entropy between the true posterior and the optimal soft predictor. 
This is a measure of "regret" or excess loss. whereby the optimal soft predictor is when this is equal, i.e. $q^*(z|y)=p(z|y)$.
The log-loss measures the "surprise" experienced by the predictor when observing $y=y$ given $z=z$.
The surprise is higher if the output is less expected

:::
