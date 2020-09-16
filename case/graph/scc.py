"""
https://blog.csdn.net/liujc_/article/details/50988432
scc: strongly connected component
- 有向图分量内，任意两个顶点连通
- 任意有向图 都能分成 若干个不相交的 scc；scc 是针对顶点而言的，顶点不相交
- 分解后的分量作为1个顶点，可以得到 DAG

dfs
"""

num_v = 5
edges = [[0, 1], [1, 0], [0, 2], [2, 0], [1, 3], [1, 4]]

adj = [[] for _ in range(num_v)]
for pre, cur in edges:
    adj[pre].append(cur)  # 邻接表出度节点


# https://my.oschina.net/u/4579195/blog/4541886
def tarjan():
    stamp = 0  # 时间戳
    stamp_dict = {}

    def dfs(u):
        nonlocal stamp
        stamp_dict[u] = stamp
        stamp += 1

        for v in adj[u]:
            dfs(v)

    dfs(0)
    print(stamp_dict)


tarjan()
