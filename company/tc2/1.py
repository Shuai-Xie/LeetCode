"""
3
9
5 4 3 2 1 2 3 4 5
5
1 2 3 4 5
14

87 70 17 12 14 86 61 51 12 90 69 89 4 65
87 70 12 12 69 89
不要求连续

8
0
6
"""

# arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]
arr = [1, 2, 3, 4, 5]
# arr = [87, 70, 17, 12, 14, 86, 61, 51, 12, 90, 69, 89, 4, 65]


# 选择增加的数 可以是 后面的...
# 对称的 最长上升子序列长度


# 倒着计算 每个值的 最长上升子序列 长度
def length_of_LIS(a):
    n = len(a)
    dp = [1] * n

    for i in range(n - 2, -1, -1):  # 倒数第2个 到 第0个
        for j in range(i + 1, n):
            if a[j] > a[i]:
                dp[i] = max(dp[i], dp[j] + 1)  # 表示 j 左侧可 以 i 为开头

    return dp


up = length_of_LIS(arr)
down = length_of_LIS(arr[::-1])[::-1]

# 找到出现次数 >=2 的元素 所在的 idxs
val_idxs = {}
for idx, val in enumerate(arr):
    if val not in val_idxs:
        val_idxs[val] = [idx]
    else:
        val_idxs[val].append(idx)

ans = 0
for idxs in val_idxs.values():
    if len(idxs) >= 2:
        for i, j in zip(idxs[:-1], idxs[1:]):  # i 左， j 右
            ans = max(ans, min(down[i], up[j]))
print(ans * 2)
