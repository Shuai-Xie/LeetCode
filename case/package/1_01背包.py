"""
https://www.acwing.com/problem/content/2/

01 背包
N 件物品，背包容量 V;
第i件物品 体积 v_i, 价值 w_i

特点：每种物品仅有一件，可以选择放或不放。

背包最多能装 多大价值物品

F[i][j]: 前 i 件物品 "恰" 放入一个容量为 j 的背包可以获得的最大价值

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

N, V = 4, 5
vs = [0] + [1, 2, 3, 4]
ws = [0] + [2, 4, 4, 5]


def f1():
    F = [[0] * (V + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, V + 1):
            F[i][j] = F[i - 1][j]  # 把不能装的情况在这里解决
            if j >= vs[i]:
                F[i][j] = max(F[i][j], F[i - 1][j - vs[i]] + ws[i])
    print(F[N][V])


def f1_():
    F = [[0] * (V + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(vs[i], V + 1):  # 能装的情况，跳过了不能装的情况
            F[i][j] = max(F[i][j], F[i - 1][j])  # 要与 F[i-1][j] 进行比较
            F[i][j] = max(F[i][j], F[i - 1][j - vs[i]] + ws[i])
    print(F[N][V])


def f2():
    F = [0] * (V + 1)

    for i in range(1, N + 1):
        # 从大到小枚举，保证 max() 内 F[j - vs[i]] 实际对应的是 F[i-1][j - vs[i]]
        # 如果正向枚举，F[j - vs[i]] 对应的是 F[i][j - vs[i]]，即当前 i 下计算的值！
        for j in range(V, vs[i] - 1, -1):  # j >= vs[i]
            F[j] = max(F[j], F[j - vs[i]] + ws[i])

    print(F[V])


"""
假如要找 恰好装满的情况？

初始化 F = [0] + [-float('inf')] * V, 确保 max 只能从 F[0]+ws[i] 型状态进行转移
如果初始化 F 都为 0，从其他状态转移过来，如 F[1] 转移，此时背包容量为 V-1
---
原始状态 F[V]: V=1...V 所有状态下的最大值
执行 F[j] = max(..) 始终可以取到 j 之前任意一个状态的最大值，即 v<j 场景，没有恰好装满 j 的场景

如果要使得 加入 vs[i] 恰好装满 j，之前的 j-vs[i] 必须也是恰好装满, 
要从 F[0]=0 这唯一一个有效状态转移，其他处于 ( j-vs[i], j) 范围内的较优解，不能参与 max 求解
而 j 是从大到小遍历，这些值初始化为 -inf，就不会取到了; 如果始终装不满，F[V] = -inf
"""

f1()
f2()
