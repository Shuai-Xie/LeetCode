"""
N 种物品, 每种 限量 s

0<N,V≤100
0<vi,wi,si≤100

O(n^3) 10^6
"""

N, V = map(int, input().split())
vs, ws, ss = [0], [0], [0]
for _ in range(N):
    v, w, s = map(int, input().split())
    vs.append(v)
    ws.append(w)
    ss.append(s)

N, V = 4, 5
vs = [0] + [1, 2, 3, 4]
ws = [0] + [2, 4, 4, 5]
ss = [0] + [3, 1, 3, 2]

# 因为有数量约束，不方便用 完全背包 的优化方式 去掉某些商品

F = [0] * (V + 1)

for i in range(1, len(vs)):
    for j in range(V, vs[i] - 1, -1):
        num = min(ss[i], j // vs[i])  # 每类商品 最多放入数量
        for k in range(1, num + 1):
            F[j] = max(F[j], F[j - k * vs[i]] + k * ws[i])
print(F[-1])
