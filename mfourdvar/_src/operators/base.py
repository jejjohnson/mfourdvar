import typing as tp
import equinox as eqx
import jax.numpy as jnp
from mfourdvar._src.operators.identity import Identity
from jaxtyping import Array, PyTree


class ObsOperator(eqx.Module):
    operator: eqx.Module

    def __init__(self, operator: tp.Callable = Identity()):
        self.operator = operator

    def __call__(self, x: Array, params: tp.Optional[PyTree] = None) -> Array:
        return self.operator(x)

    def loss(
        self, 
        x: Array, 
        y: Array, 
        mask: tp.Optional[Array] = None,
        params: tp.Optional[PyTree] = None
    ) -> Array:
        y_pred = self(x, params=params)
        # nans to numbers
        y = jnp.nan_to_num(y)

        if mask is not None:
            loss = jnp.sum(mask * (y_pred - y) ** 2)
        else:
            loss = jnp.sum((y_pred - y) ** 2)

        return loss
