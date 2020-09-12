"""
输出 最优选法的方案数, 要知道 max_value 对应多少情况

f[i] 用来存储背包容积为 i 时的最佳方案的总价值
g[i] 为背包容积为 i 时总价值为最佳的方案数

g[i] = 所有 f[j] = f[i] 的 方案数之和?
"""

# N, V = map(int, input().split())
# vs, ws = [0], [0]
# for _ in range(N):
#     v, w = map(int, input().split())
#     vs.append(v)
#     ws.append(w)

N, V = 4, 5
vs = [0] + [1, 2, 3, 4]
ws = [0] + [2, 4, 4, 6]

f = [0] * (V + 1)
g = [1] * (V + 1)  # 商品数量为0，全不装，方案=1

mod = 1e9 + 7

for i in range(1, N + 1):
    for j in range(V, vs[i] - 1, -1):  # j >= vs[i]
        value = f[j - vs[i]] + ws[i]
        if value > f[j]:
            f[j] = value
            g[j] = g[j - vs[i]]  # j 从 j-vs[i] 转移过来，方案数相等
        elif value == f[j]:  # 此时 f[j] 表示没有 vs[i] 的价值，与有 vs[i] 价值一样，所以方案数相加
            g[j] += g[j - vs[i]]  # 方案数多一倍

        g[j] = int(g[j] % mod)
        # 不装状态，还对应 i-1 时刻的方案

print(g[-1])
