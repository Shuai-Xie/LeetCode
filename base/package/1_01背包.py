"""01 背包
N 件物品，背包容量 V
每件物品 选 or 不选
物品体积 v_i, 价值 w_i

背包最多能装 多大价值物品

F[i][j]: 前 i 件物品，容量为 j 时能获得的最大价值

F[i][j] = max(
    F[i-1][j],              # 第 i 件不装
    F[i-1][j-v_i] + w_j     # 装
)

二维过程：
i: 物品件数 逐渐增多
j: 背包容量 逐渐变大
"""

N, V = map(int, input().split())
vs, ws = [0], [0]
for _ in range(N):
    v, w = map(int, input().split())
    vs.append(v)
    ws.append(w)


def solver1():
    # N+1 * V+1 矩阵
    F = [[0] * (V + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        # i 个物品
        # 背包容量由 1 ~ V 分别的最优解
        for j in range(1, V + 1):
            if j >= vs[i]:  # 判断当前容量 能装下 i
                F[i][j] = max(
                    F[i - 1][j],  # 不装第 1 个
                    F[i - 1][j - vs[i]] + ws[i],  # 装第i个
                )
            else:
                F[i][j] = F[i - 1][j]

    print(F[N][V])


def solver2():
    F = [0] * (V + 1)

    for i in range(1, N + 1):
        for j in range(V, vs[i] - 1, -1):  # j >= vs[i]
            F[j] = max(F[j], F[j - vs[i]] + ws[i])

    print(F[V])


solver2()
