"""
si
-1 每类物品 放 1 次
0，无限次
>0 指定次
"""

N, V = map(int, input().split())
vs, ws = [0], [0]
for _ in range(N):
    v, w, s = map(int, input().split())  # 将 s 个 v 二进制拆分为不同虚拟物品
    if s == -1:  # 01
        vs.append(v)
        ws.append(w)
    else:
        if s == 0:  # 无限次
            s = V // v
        else:  # 指定次
            s = min(V // v, s)  # 有效数量
        k = 1
        while k <= s:
            vs.append(k * v)
            ws.append(k * w)
            s -= k  # 更新 s 剩余量
            k *= 2  # k 提升进制
        if s > 0:
            vs.append(s * v)
            ws.append(s * w)

# 转化为 二进制拆分后的 01 背包问题
F = [0] * (V + 1)
for i in range(1, len(vs)):
    for j in range(V, vs[i] - 1, -1):  # 01 背包，只能装1个，所以是对的
        F[j] = max(F[j], F[j - vs[i]] + ws[i])
print(F[-1])
