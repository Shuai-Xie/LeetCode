"""
https://leetcode-cn.com/problems/network-delay-time/

从 K 发出信号，问需要多久使 所有节点都收到信息，如不能返回 -1
"""

from typing import List
import heapq
import collections


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 邻接表
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}  # 直接将顶点是否在 S 也判断了
        heap = [(0, K)]  # cost, v;
        # 注意 heapq 使用的 key 为字典序，cost 在前

        while heap:
            cost, u = heapq.heappop(heap)
            if u in dist:  # 判断节点是否已加入 S
                continue
            dist[u] = cost
            for v, w in graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (cost + w, v))  # 添加元素时 即以调整 list，保证堆结构不变

        return max(dist.values()) if len(dist) == N else -1


# times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
# N = 4
# K = 2
# times = [[1, 2, 1], [2, 1, 3]]
# N = 2
# K = 2
times = [[2, 4, 10], [5, 2, 38], [3, 4, 33], [4, 2, 76], [3, 2, 64], [1, 5, 54], [1, 4, 98], [2, 3, 61], [2, 1, 0], [3, 5, 77], [5, 1, 34], [3, 1, 79],
         [5, 3, 2], [1, 2, 59], [4, 3, 46], [5, 4, 44], [2, 5, 89], [4, 5, 21], [1, 3, 86], [4, 1, 95]]
N = 5
K = 1
s = Solution()
print(s.networkDelayTime(times, N, K))
