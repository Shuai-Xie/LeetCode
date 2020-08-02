"""
对于给定的二维矩阵，矩阵的维度是m*m，
获得其极大值点及其相应位置。（注：一个矩阵有可能有多个极大值。）
"""
import numpy as np


def get_max_val(a):
    h, w = a.shape

    max_val, max_pos = [], []

    # 增加一圈 全是很小的值
    MIN = -2 ** 31
    a = np.pad(a, ((1, 1), (1, 1)), constant_values=MIN)  # 对应矩阵每个维度的填充

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if a[i][j] > a[i - 1][j] and a[i][j] > a[i + 1][j] and a[i][j] > a[i][j - 1] and a[i][j] > a[i][j + 1]:
                max_val.append(a[i][j])
                max_pos.append((i - 1, j - 1))

    return max_val, max_pos


# a = np.array([
#     [1, 2, 4],
#     [1, 5, 4],
#     [7, 2, 4]
# ])
a = np.random.rand(10, 10)
a = np.around(a, decimals=2)
print(a)
max_val, max_pos = get_max_val(a)
print(max_val)
print(max_pos)
