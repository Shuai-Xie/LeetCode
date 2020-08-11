"""
随机数生成 洗牌算法
生成 1-n 范围内的随机数
"""
import random


def shuffle(x):
    for i in range(len(x)):
        # 从 x[:i+1] 中随机选1个 与 x[i] 交换
        # 保证每次 随机取到的数 都与当前的数不同. O(n)
        # 传统做法：每次随机取一个，都从数组中删除这个数，但是删除操作也是O(n)，最终为 O(n^2)
        idx = int(random.random() * i) + 1
        x[idx], x[i] = x[i], x[idx]


n = 10
x = list(range(1, n + 1))
print(x)
for _ in range(5):
    shuffle(x)  # list 传入引用
    print(x)
