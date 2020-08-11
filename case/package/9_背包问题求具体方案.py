"""
输出字典序最小的方案:
最优解中所选物品的编号序列，且该编号序列的字典序最小

# 字典序，从头到尾排序，按查字典的方式
# python sorted 方法，多键值元素排序，本身就是从高位到低位 字典排序

8: 表明同样价值 可有多种方案；从中选出字典序最小的
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


# 可以保存 g 的所有方案，但内存会爆
def f1():
    f = [0] * (V + 1)  # 价值
    g = [[] for _ in range(V + 1)]  # 每个价值下的所有方案，因为后序状态可能是从 之前前.. 的方案转移过来

    # 都是 = > 两种不同情况下
    # 需要 记录 不同的方案
    for i in range(1, len(vs)):  # 商品
        for j in range(V, vs[i] - 1, -1):  # 容量
            value = f[j - vs[i]] + ws[i]
            if value > f[j]:  # g[j] 更新为 g[j - vs[i]] 下一个状态
                f[j] = value
                if not g[j - vs[i]]:
                    g[j] = [[i]]
                else:
                    g[j] = [li + [i] for li in g[j - vs[i]]]  # 原始方案添加新元素
            elif value == f[j]:
                # 要在原来 g[j] 基础上添加新方案, 因为原来的 g[j] 是不包括 vs[i] 的
                # 不管原来的 g[j] 是空 还是 别的，都直接 append
                # 从 g[j - vs[i]] 转移的 g[j]
                if not g[j - vs[i]]:
                    g[j].append([i])
                else:
                    for li in g[j - vs[i]]:
                        g[j].append(li + [i])

            # 每种方案 都只存储字典序最小的，节省空间? 因为在这些基础上的后序延长串 仍是从这些开始
            if len(g[j]) > 1:
                g[j].sort()
                g[j] = [g[j][0]]  # 仍要保持为 list

    print(*g[-1][0])


def f2():
    f = [0] * (V + 1)  # 价值
    g = [[] for _ in range(V + 1)]  # 每个价值只保存 1 个方案，有字典序要求在，即便同价值也会分开

    # 都是 = > 两种不同情况下
    # 需要 记录 不同的方案
    for i in range(1, len(vs)):  # 商品
        for j in range(V, vs[i] - 1, -1):  # 容量
            value = f[j - vs[i]] + ws[i]
            if value > f[j]:  # g[j] 更新为 g[j - vs[i]] 下一个状态
                f[j] = value
                g[j] = g[j - vs[i]] + [i]  # 原始方案添加新元素
            elif value == f[j]:
                # 比较新老方案的 字典序, min(新,老)
                g[j] = min(g[j - vs[i]] + [i], g[j])

    print(*g[-1])


f1()
f2()
