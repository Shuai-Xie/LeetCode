"""
N 种物品, 每种不限量
"""
# N, V = map(int, input().split())
# vs, ws = [0], [0]
# for _ in range(N):
#     v, w = map(int, input().split())
#     vs.append(v)
#     ws.append(w)

N, V = 4, 5
vs = [0] + [1, 2, 3, 4]
ws = [0] + [2, 4, 4, 5]


def f1():  # 2维空间
    F = [[0] * (V + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(vs[i], V + 1):  # 直接从能取到的 j 开始
            F[i][j] = F[i - 1][j]  # 不放
            for k in range(1, 1 + j // vs[i]):  # 当前容量 j 下，物品 i 可放入的个数范围; 其实如果 k 从0开始，就涵盖了 F[i-1][j] 的比较
                F[i][j] = max(F[i][j], F[i - 1][j - k * vs[i]] + k * ws[i])
    print(F[-1][-1])


def f2():  # 1维空间
    F = [0] * (V + 1)
    for i in range(1, N + 1):
        for j in range(V, vs[i] - 1, -1):  # range 都是 end 取不到
            # 此时 F[j] 表示上轮 i-1 的最优解; 也是 k=0 的最优解
            for k in range(1, 1 + j // vs[i]):
                F[j] = max(F[j], F[j - k * vs[i]] + k * ws[i])  # 注意 k*
    print(F[-1])


# 优化1
def f3():
    discards = set()
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):  # 其实有比较冗余
            # 优化：重量轻，且价值 >= 后者; 不能用平均价值，比如剩 3; 4/2 >= 5/3, 此时装 3 恰好包满，而装2不满
            if vs[i] <= vs[j] and ws[i] >= ws[j]:
                discards.add(j)
    for idx, v in enumerate(sorted(discards)):  # 从前到后保存
        vs.pop(v - idx)  # 每删除1个，idx 在原始基础上 -1
        ws.pop(v - idx)

    # print(vs)  # 可以看到去掉了 3 号物品
    # print(ws)

    F = [0] * (V + 1)
    for i in range(1, len(vs)):
        for j in range(V, vs[i] - 1, -1):  # 从大到小枚举
            for k in range(1, 1 + j // vs[i]):
                F[j] = max(F[j], F[j - k * vs[i]] + k * ws[i])
    print(F[-1])


# 优化2
# 转成 01 背包，商品 i 认为有 V//v[i] 个完全一样的商品；去掉 k for 循环
def f4():
    F = [0] * (V + 1)
    for i in range(1, len(vs)):
        for j in range(vs[i], V + 1):  # v 正向, max() 表示 F[j-vs[i]] 为 F[i][j-vs[i]], 然后 j 逐渐增加，就包含了i物品所有 1..V/vs[i] 场景
            F[j] = max(F[j], F[j - vs[i]] + ws[i])
    print(F[-1])


# 优化3
# 根据背包容量上限，转化成多重背包二进制方案: 转化后，可涵盖所有情况 1..V 之间的背包容量, 即 F[j] 子问题都可涵盖
def f5():
    vss, wss = [0], [0]
    for i in range(1, len(vs)):
        v, w = vs[i], ws[i]
        s = V // v  # 背包能装每个物体 v 的上限
        k = 1
        while k <= s:
            vss.append(v * k)
            wss.append(w * k)
            s -= k
            k *= 2
        if s > 0:
            vss.append(v * k)
            wss.append(w * k)

    F = [0] * (V + 1)
    # 二进制后，转为 01 背包, 能涵盖 按照s均分的所有场景
    for i in range(1, len(vss)):
        for j in range(V, vss[i] - 1, -1):
            F[j] = max(F[j], F[j - vss[i]] + wss[i])
    print(F[-1])


f1()
f2()
f3()
f4()
f5()
