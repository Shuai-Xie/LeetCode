import numpy as np


# 向量范数
def vector_norm():
    x = np.random.rand(10)  # *dn, 不要 (), 如 np.random.rand(10,10)
    print(x)

    # x_norm = np.linalg.norm(x, ord=np.inf)  # max
    x_norm = np.linalg.norm(x, ord=-np.inf)  # min
    print(x_norm)

    x_norm = np.linalg.norm(x, ord=0)  # 0范数 恰好为非0元素个数
    print(x_norm)


# 矩阵范数
def get_rand_int_matrix(shape, min, max):
    a = np.random.random(shape) * (max - min) + min  # 表示从 min 开始
    return a.astype(int)


A = get_rand_int_matrix((3, 3), min=-10, max=10)
print(A)

# 1, 列和范数，列向量 绝对值之和 的最大值
print(np.linalg.norm(A, ord=1))

print(0 ** 0)
print(1 ** 0)
