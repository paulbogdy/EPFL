# -*- coding: utf-8 -*-
"""a function used to compute the loss."""

import numpy as np

def mse(e):
    return 1/(2*len(e)) * np.dot(e, e)

def mae(e):
    return 1/(2*len(e)) * np.sum(np.abs(e))

def compute_loss(y, tx, w, loss=mse):
    """Calculate the loss using either MSE or MAE.

    Args:
        y: shape=(N, )
        tx: shape=(N,2)
        w: shape=(2,). The vector of model parameters.

    Returns:
        the value of the loss (a scalar), corresponding to the input parameters w.
    """
    e = tx @ w - y
    return loss(e)
