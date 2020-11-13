"""
给定有向无权图，判断两个节点之间是否存在一条路径
图中可能存在自环和平行边

提交过程发现：dfs 总是比 bfs 搜索更快；无论是 recur 还是 stack
"""
from typing import List


class Solution:

    def findWhetherExistsPath_dfs_recur(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        # 图转邻接表
        adj = [[] for _ in range(n)]
        for u, v in graph:
            adj[u].append(v)

        def dfs(start, target):
            if start == target:
                return True
            return any([dfs(s, target) for s in adj[start]])

        return dfs(start, target)

    def findWhetherExistsPath_bfs(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        # 图转邻接表
        adj = [[] for _ in range(n)]
        for u, v in graph:
            adj[u].append(v)

        queue = [start]
        visited = set()

        while queue:
            u = queue.pop(0)  # 队首
            if u == target:
                return True
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    queue.append(v)
        return False

    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        # 图转邻接表
        adj = [[] for _ in range(n)]
        for u, v in graph:
            adj[u].append(v)

        stack = [start]
        visited = set()

        while stack:
            u = stack.pop()  # 栈顶
            if u == target:
                return True
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    stack.append(v)
        return False


# n = 3
# graph = [[0, 1], [0, 2], [1, 2], [1, 2]]
# start = 0
# target = 2

n = 5
graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]
start = 0
target = 4

s = Solution()
print(s.findWhetherExistsPath(n, graph, start, target))
