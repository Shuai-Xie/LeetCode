from typing import List
import collections


class Solution:

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        times[i] = (u, v, w); u->v 有向, w 时长
            从某个节点 K 发出一个信号。需要多久才能 使所有节点 都收到信号？
            如果不能使所有节点收到信号，返回 -1
        N: 节点总数
        K: 选取的节点，从 k 出发
        """
        # 建图，节点链表形式，存储每个节点的出度路径
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))  # w 在前，后文 sort 按照 w 排序

        dist = {  # 存储 K 到各个 v 的最小时长
            v: float('inf') for v in range(1, N + 1)
        }

        # dfs 递归出口有2个
        # 1. 路径到 node 时长 >= 已记录时长; 如果未大于，则更新得到更小时长
        # 2. 邻接节点在 for 中遍历完了
        # for 相当于在走图中所有可行路径
        def dfs(node, elapsed):  # dfs: 到达 node 时 elapsed 经过的时长
            # 剪枝
            # dfs 到 node 的时长 > 已存路径的时长，那么这条路 + node 之后的路 都是长时间的，剪掉
            if elapsed >= dist[node]:
                return

            dist[node] = elapsed

            # 遍历当前 node 的所有可走方向
            for time, nxt in sorted(graph[node]):  # sort 贪心思想，从最短的出发, dfs 寻找，这样后文再出现的长时间可能及早 return
                dfs(nxt, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1

    def networkDelayTime2(self, times: List[List[int]], N: int, K: int) -> int:
        """
        Dijkstra 单源最短路径，找到当前节点到图中所有节点的最短路径，DP 思想
            每次扩展一个据 K 最近的点，更新与其相邻点的距离
        """
        pass
