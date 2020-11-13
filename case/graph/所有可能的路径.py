"""
有向无环图，从 0 到 n-1 的所有路径
"""
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)  # graph 即以邻接表形式 表示图的临接边
        res = []
        path = []

        def dfs(i):
            path.append(i)
            if i == n - 1:
                res.append(path[:])
                return
            for v in graph[i]:  # 遍历 i 邻接点
                dfs(v)
                path.pop()  # dfs 终止后，pop 添加的元素，回溯到上一个可以 for 遍历其他路径的位置

        dfs(0)
        return res


# graph = [[1, 2], [3], [3], []]
# graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
# graph = [[1], []]
graph = [[1, 2, 3], [2], [3], []]

s = Solution()
print(s.allPathsSourceTarget(graph))
