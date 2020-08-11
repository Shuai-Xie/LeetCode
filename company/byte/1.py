n, m = 8, 1
s = 'aabaabaa'

# m <= n
F = [[0] * (n + 1) for _ in range(m + 1)]  # 外循环 字母数量

for i in range(1, m + 1):  # 修改字母的个数?
    for j in range(1, n + 1):  # 字符串长度

