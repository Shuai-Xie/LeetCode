from typing import List

"""
想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1], 1 -> 0

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
判断是否有的课程先决不能满足?
"""


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :param numCourses: 课程总数
        :param prerequisites: 先决条件，有向边 (u,v); v->u 反向 拓扑结果正向
        只给出 prerequisites，可能是 多个子图
        """
        # 转邻接表
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)

        visited = [0] * numCourses

        def dfs(u):
            if visited[u] == 1:  # 终止条件
                return False
            if visited[u] == 2:  # 完全遍历完的节点，状态正确
                return True

            visited[u] = 1
            for v in adj[u]:
                if not dfs(v):
                    return False
            visited[u] = 2  # 完全遍历完
            return True  # 正常遍历完

        for i in range(numCourses):  # 每个节点都要判断
            if not dfs(i):  # 完成1个连通分量(深度优先树)的染色; 对于此分量内节点 visited=2，下轮 for 直接返回 true
                return False

        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 如果存在 返回拓扑排序序列; 如果不存在 返回 []
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)

        visited = [0] * numCourses
        finish_t = [0] * numCourses

        time = 0

        def dfs(u):
            nonlocal time
            if visited[u] == 1:  # 终止条件
                return False
            if visited[u] == 2:  # 完全遍历完的节点，状态正确
                return True

            visited[u] = 1
            time += 1
            for v in adj[u]:
                if not dfs(v):
                    return False
            visited[u] = 2  # 完全遍历完
            time += 1
            finish_t[u] = time
            return True  # 正常遍历完

        flag = True
        for i in range(numCourses):
            if not dfs(i):  # 存在环
                flag = False

        if flag:
            return sorted(range(numCourses), key=lambda t: finish_t[t], reverse=True)  # 反向结果
        else:
            return []


s = Solution()
cases = [
    [2, [[1, 0]]],
    [3, [[1, 0], [1, 2], [0, 1]]],
    [3, [[0, 2], [1, 2], [2, 0]]],
    [7, [[1, 0], [2, 0], [4, 3], [5, 3], [6, 2], [6, 4]]]
]

for num_v, edges in cases:
    print(s.canFinish(num_v, edges), s.findOrder(num_v, edges))
