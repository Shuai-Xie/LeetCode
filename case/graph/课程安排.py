"""
拓扑过程，给的图是有向图

判断 课程对中，0 是否是 1 的先修课程
    先修，就是判断 0..1 之间是否存在路径
"""

from typing import List


class Solution:

    def checkIfPrerequisite_dfs(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(start, end):
            stack = [start]
            visited = set()

            while stack:
                u = stack.pop()  # 栈顶
                if u == end:
                    return True
                visited.add(u)
                for v in adj[u]:
                    if v not in visited:
                        stack.append(v)
            return False

        return [dfs(*q) for q in queries]

    def checkIfPrerequisite_dfs2(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(start, end):
            if start == end:
                return True
            return any([dfs(v, end) for v in adj[start]])  # 某1个element=True 即 return True

        return [dfs(*q) for q in queries]

    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # dfs + memo
        adj = [[] for _ in range(n)]
        for u, v in prerequisites:
            adj[u].append(v)

        memo = {}

        def dfs(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            stack = [start]
            visited = set()

            while stack:
                u = stack.pop()  # 栈顶
                if u == end:
                    return True
                visited.add(u)
                memo[(start, u)] = True
                for v in adj[u]:
                    if v not in visited:
                        stack.append(v)
            return False

        return [dfs(*q) for q in queries]

    def checkIfPrerequisite_floyd(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[False] * n for _ in range(n)]
        for u, v in prerequisites:
            dp[u][v] = True  # 有通路即为 True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if not dp[i][j]:  # 跳过已经判断有路径的
                        dp[i][j] = dp[i][k] and dp[k][j]

        return [dp[i][j] for i, j in queries]


# n = 2
# prerequisites = [[1, 0]]
# queries = [[0, 1], [1, 0]]
#
# n = 2
# prerequisites = []
# queries = [[1, 0], [0, 1]]

n = 5
prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]]
queries = [[0, 4], [4, 0], [1, 3], [3, 0]]

s = Solution()
print(s.checkIfPrerequisite_dfs(n, prerequisites, queries))
print(s.checkIfPrerequisite_floyd(n, prerequisites, queries))
