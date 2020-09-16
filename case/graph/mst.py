"""
MST Minimum Spanning Tree
贪心思想
    Kruskal: 寻找连接 森林中 两棵子树的 权值最小的边
    Prim: 寻找子树 A 连接外部顶点中 权值最小的边
"""

num_v = 9
edges = [
    # node1, node2, cost
    ['a', 'b', 4],  # 编号 node2 > node1, 就不会重复添加边 
    ['a', 'h', 8],
    ['b', 'c', 8],
    ['b', 'h', 11],
    ['c', 'd', 7],
    ['c', 'f', 4],
    ['c', 'i', 2],
    ['d', 'e', 9],
    ['d', 'f', 14],
    ['e', 'f', 10],
    ['f', 'g', 2],
    ['g', 'h', 1],
    ['g', 'i', 6],
    ['h', 'i', 7],
]

edges = sorted(edges, key=lambda t: t[-1])  # 按 cost 排序
parent = list(range(num_v))  # 存储顶点的 idx; 使用 idx 索引当前节点的代表 idx，表示其属于某个连通分量


def node2idx(c):  # 字母节点 转 idx
    return ord(c) - ord('a')


def find_parent(idx):  # 节点 idx
    if idx == parent[idx]:  # 自身就是父母
        return idx
    return find_parent(parent[idx])  # 回溯找到最初的父母


def Kruskal():
    mst_cost = 0
    mst = []

    # edges 排序过，保证每次 parent a/b 不同的边(即属于两个不同连通分量的边) 是所有边中最小的
    for e in edges:
        pa = find_parent(node2idx(e[0]))  # parent idx
        pb = find_parent(node2idx(e[1]))

        if pa != pb:  # 说明 e 是属于两个森林的最小边
            mst_cost += e[-1]
            mst.append(e)
            parent[pa] = pb  # 将 a 划入 b 子树

    print(mst_cost)
    print(sorted(mst))
