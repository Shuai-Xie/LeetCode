"""
二进制优化?

0<N≤1000
0<V≤2000
0<vi,wi,si≤2000

O(n^3), 10^9
"""

"""
多重 -> 01, 物体数量 = sum(ss), 仍然是 O(n^3), 此时 N = N * S 所以还是 O(n^3)

二进制拆法? 让 k 循环迭代次数减少到 log(s[i]) 向上取整; 降低了复杂度 2000 ~ 2^11, -> 10^7

本质：以 v[i] 为进制，所能表示的所有 <= s[i] * v[i] 的数，涵盖了所有情况, 如 v[i], 2[i], 3v[i]
拆分成：v[i], 2v[i], 4[vi] ...，涵盖了所有背包的容量情况

7
1 2 4
0 ~ 7

10
1 2 4 3  # 所有的数 选或者不选 刚好能凑到 0-10 中任一种状态; 数字对应二进制所在位，所以能表示范围内任一数字
0 ~ 10

last_num = s - 1 - 2 - 4 # 直到差为负值， last_num 表示二进制的最低位
"""

N, V = map(int, input().split())
vs, ws = [0], [0]
for _ in range(N):
    v, w, s = map(int, input().split())  # 将 s 个 v 二进制拆分为不同虚拟物品
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
