# N 种物品
N, V = map(int, input().split())
vs, ws = [0], [0]
for _ in range(N):
    v, w = map(int, input().split())
    vs.append(v)
    ws.append(w)

F = [[0] * (V + 1) for _ in range(N + 1)]

for i in range(1, N + 1):  # N 种
    for j in range(1, V + 1):  # 容量
        base = 0
        for k in range(j // vs[i]):  # 第 i 件物品，最多可放的个数
            if j - k * vs[i] >= 0:  # 当前容量能放下
                base = max(base, F[i - 1][j - k * vs[i]] + k * ws[i])
        F[i][j] = base

print(F[N][V])
