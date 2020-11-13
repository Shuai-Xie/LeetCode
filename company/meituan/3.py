"""
最长连续上升子序列，并且 可以取模
"""

# 数据组数
# T = int(input())
#
# for _ in range(T):
#     N = int(input())
#     a = list(map(int, input().split()))


a = [3, -2, 4, -1]
N = 4


def sum_ij(i, j):
    s = 0
    for k in range(i, j):
        s += a[k % N]
    return s


res = 0
for i in range(N - 1):
    if a[i] < 0:
        continue
    for j in range(i, i + N):
        res = max(res, sum_ij(i, j))

print(res)
