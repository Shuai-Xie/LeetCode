"""
有 N 件物品和一个容量是 V 的背包，背包能承受的最大重量是 M。
每件物品只能用一次。体积是 vi，重量是 mi，价值是 wi。
01
除了容量约束，还有 重量约束
"""

N, V, M = map(int, input().split())
vs, ms, ws = [0], [0], [0]
for _ in range(N):
    v, m, w = map(int, input().split())  # 体积，重量，价值
    vs.append(v)
    ms.append(m)
    ws.append(w)

# N, V, M = 4, 5, 6
# vs = [0] + [1, 2, 3, 4]
# ms = [0] + [2, 4, 4, 5]
# ws = [0] + [3, 4, 5, 6]

# F = [[0] * (M + 1)] * (V + 1)  # 这样定义是错误的！list 可变对象，引用调用，k 循环体更新1个值，连带 V+1 行都会变化!
F = [[0] * (M + 1) for _ in range(V + 1)]

for i in range(1, len(vs)):
    for j in range(V, vs[i] - 1, -1):  # 背包容量下限
        for k in range(M, ms[i] - 1, -1):  # 重量下限
            F[j][k] = max(F[j][k], F[j - vs[i]][k - ms[i]] + ws[i])

print(F[-1][-1])
