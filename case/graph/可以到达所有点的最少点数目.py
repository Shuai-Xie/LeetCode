"""
https://leetcode-cn.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

有向无环图，找到最小的点集 从这些点出发能到 图中所有其他点
这些可达点的 并集 能组成 全集

题目保证解存在且唯一

寻找 入度为 0 的点即可
因为这些点 是没有路径到来的啊！只能作为起点出发
"""

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1

        return [i for i in range(n) if indegree[i] == 0]


# n = 6
# edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
n = 5
edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
s = Solution()
print(s.findSmallestSetOfVertices(n, edges))
