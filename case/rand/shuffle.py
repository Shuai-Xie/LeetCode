"""
随机数生成 洗牌算法; 生成随机序列
"""
import random


def shuffle(arr):
    n = len(arr)

    for i in range(1, n):
        rand_idx = int(random.random() * i)  # [0, i-1]
        arr[rand_idx], arr[i] = arr[i], arr[rand_idx]  # 将 i 与之前 某个位置的数 交换


n = 10
x = list(range(1, n + 1))

random.seed(10)
for _ in range(5):
    shuffle(x)  # list 传入引用
    print(x)
