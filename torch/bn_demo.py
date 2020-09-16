"""
https://kratzert.github.io/2016/02/12/understanding-the-gradient-flow-through-the-batch-normalization-layer.html
"""
import numpy as np


def batchnorm_forward(x, gamma, beta, eps):
    N, D = x.shape

    # step1: calculate mean
    mu = 1. / N * np.sum(x, axis=0)

    # step2: subtract mean vector of every trainings example
    xmu = x - mu

    # step3: following the lower branch - calculation denominator
    sq = xmu ** 2

    # step4: calculate variance
    var = 1. / N * np.sum(sq, axis=0)

    # step5: add eps for numerical stability, then sqrt
    std = np.sqrt(var + eps)

    # step6: invert std
    inv_std = 1. / std

    # step7: execute normalization
    xhat = xmu * inv_std

    # step8: Nor the two transformation steps
    gammax = gamma * xhat

    # step9
    out = gammax + beta

    # store intermediate
    cache = (xhat, gamma, xmu, inv_std, std, var, eps)

    return out, cache


def batchnorm_backward(dout, cache):
    # unfold the variables stored in cache
    xhat, gamma, xmu, inv_std, std, var, eps = cache

    # get the dimensions of the input/output
    N, D = dout.shape

    # step9
    dbeta = np.sum(dout, axis=0)
    dgammax = dout  # not necessary, but more understandable

    # step8
    dgamma = np.sum(dgammax * xhat, axis=0)
    dxhat = dgammax * gamma

    # step7
    dinv_std = np.sum(dxhat * xmu, axis=0)
    dxmu1 = dxhat * inv_std

    # step6
    dstd = -1. / (std ** 2) * dinv_std

    # step5
    dvar = 0.5 * 1. / np.sqrt(var + eps) * dstd

    # step4
    dsq = 1. / N * np.ones((N, D)) * dvar

    # step3
    dxmu2 = 2 * xmu * dsq

    # step2
    dx1 = (dxmu1 + dxmu2)
    dmu = -1 * np.sum(dxmu1 + dxmu2, axis=0)

    # step1
    dx2 = 1. / N * np.ones((N, D)) * dmu

    # step0
    dx = dx1 + dx2

    return dx, dgamma, dbeta
