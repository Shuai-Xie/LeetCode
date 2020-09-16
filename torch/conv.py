"""
https://blog.csdn.net/u014261408/article/details/105077341
"""
import numpy as np
from collections.abc import Iterable


def img2col(x, kernel_size, stride):
    """
    input: B,C,H,W
    output: B,C,
    """
    b, c, h, w = x.shape
    if not isinstance(kernel_size, Iterable):
        kernel_size = [kernel_size, kernel_size]
    hk, wk = kernel_size

    rows = (h - hk) // stride + 1
    cols = (w - wk) // stride + 1

    out = np.zeros((b, c, hk * wk, rows * cols))

    for i in range(rows):
        for j in range(cols):
            out[:, :, :, i * rows + j] = x[:, :, i:i + hk, j:j + wk].flatten()  # matrix2vector

    return out


x = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]).reshape((1, 1, 3, 3))

y = img2col(x, 2, 1)
print(y)
