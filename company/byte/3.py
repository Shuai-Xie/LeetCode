n = int(input())

inputs = []

for i in range(n):
    hi, wi = map(int, input().split())  # 牌 高度，宽度
    inputs.append([hi, wi])

dp = [0] * n

inputs.sort(key=lambda t: (-t[0], -t[1]))  # 从大到小

import random
