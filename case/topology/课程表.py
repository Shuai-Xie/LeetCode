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

        visited = [0] * numCourses  # 白色

        def dfs(u):
            if visited[u] == 1:  # 终止条件
                return False
            if visited[u] == 2:  # 完全遍历完的节点，状态正确
                return True

            visited[u] = 1  # 灰色
            for v in adj[u]:
                if not dfs(v):
                    return False
            visited[u] = 2  # 完全遍历完, 黑色
            return True  # 正常遍历完

        for i in range(numCourses):  # 每个节点 作为起点 都要判断是否会构成环路
            if not dfs(i):  # 完成1个连通分量(深度优先树)的染色; 对于此分量内节点 visited=2，下轮 for 直接返回 true
                return False

        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 如果存在 返回拓扑排序序列; 如果不存在 返回 []
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegree[cur] += 1  # 计算当前节点 cur 的入度数量, Note: 只有入度为0才能作为起点！

        visited = [0] * numCourses
        finish_t = [0] * numCourses  # 记录了每个节点访问用时

        time = 0
        invisited = [0] * numCourses

        def dfs(u):
            nonlocal time
            if visited[u] == 1:  # 终止条件
                return False
            if visited[u] == 2:  # 完全遍历完的节点，状态正确
                return True

            visited[u] = 1  # 灰色 压栈节点
            if indegree[u] > 0:  # 内部点(invisited=indegree), 计算 invisited 数量
                invisited[u] += 1
            time += 1
            for v in adj[u]:
                if not dfs(v):  # 又访问到栈内节点 visited=1
                    return False
            time += 1
            if invisited[u] == indegree[u]:
                visited[u] = 2  # 完全遍历完
                finish_t[u] = time
            else:
                visited[u] = 0  # 下次还可以继续遍历
            return True  # 正常遍历完

        flag = True
        for i in range(numCourses):
            if indegree[i] == 0 and not dfs(i):  # 存在环
                flag = False
                break

        if flag:
            print(finish_t)  # 增加 visited times 是否等于入度?
            print(invisited)
            print(indegree)
            return sorted(range(numCourses), key=lambda t: finish_t[t], reverse=True)  # 反向结果
        else:
            return []

    def find_each_Order(self, numCourses: int, prerequisites: List[List[int]]):
        # 如果存在 返回拓扑排序序列; 如果不存在 返回 []
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegree[cur] += 1  # 计算当前节点 cur 的入度数量, Note: 只有入度为0才能作为起点！

        visited = [0] * numCourses  # 节点访问状态
        finish_t = [0] * numCourses  # 节点访问用时
        invisited = [0] * numCourses  # 节点访问次数; 对应入度 来判断是否前驱任务都完成了

        def dfs(u):
            nonlocal time
            if visited[u] == 1:  # 终止条件
                return False
            if visited[u] == 2:  # 完全遍历完的节点，状态正确
                return True

            if indegree[u] > 0:  # 内部点(invisited=indegree), 计算 invisited 数量
                invisited[u] += 1

            visited[u] = 1  # 灰色 压栈节点
            time += 1
            for v in adj[u]:
                if not dfs(v):  # 又访问到栈内节点 visited=1
                    return False
            time += 1

            # 考虑到1个节点有多个先决条件的情况
            if invisited[u] == indegree[u]:  # 只有在完全遍历完 才更新 finish_t，才会被下面 node_idxs 加入
                visited[u] = 2
                finish_t[u] = time
            else:
                visited[u] = 0  # 下次还可以继续遍历; 此时 finish_t 依然为 0，不会添加入子连通分量的遍历

            return True  # 正常遍历完

        cand_select = [True] * numCourses
        topos = []
        for i in range(numCourses):
            time = 0  # 每个分量计算起点 time 归零
            if indegree[i] == 0 and dfs(i):  # 是 有向连通分量
                node_idxs = []
                for c in range(numCourses):
                    if cand_select[c] and finish_t[c] > 0:  # 已经记录时长
                        node_idxs.append(c)
                        cand_select[c] = False  # 下轮不再选F
                if len(node_idxs) > 0:
                    topos.append(sorted(node_idxs, key=lambda t: finish_t[t], reverse=True))

        print(topos)


s = Solution()
cases = [
    # [2, [[1, 0]]],
    # [3, [[1, 0], [1, 2], [0, 1]]],
    # [3, [[0, 2], [1, 2], [2, 0]]],
    [7, [[1, 0], [2, 0], [4, 3], [5, 3], [6, 2], [6, 4]]],
    # [5, [[1, 0], [2, 0], [4, 3]]],
    # [5, [[1, 0], [2, 0], [0, 2], [4, 3]]],  # 有环路的分量 没有路径
    # 各个连通分量 可以并行开始执行;
    # 内部 finish_t 应为全局 time 在累加，所以无法根据 t 判断 哪些任务可以并行; 但是同层节点的邻接点一般是并行的
]

for num_v, edges in cases:
    # print(s.canFinish(num_v, edges), s.findOrder(num_v, edges))
    s.find_each_Order(num_v, edges)
