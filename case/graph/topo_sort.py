from typing import List


class Topo:
    def find_each_Order(self, numCourses: int, prerequisites: List[List[int]]):
        """
        :param numCourses: 节点总数
        :param prerequisites: 节点间依赖关系 u -> v  [v,u] # v 依赖 u
        :return: 每个连通分量的 遍历序列

        dfs 使用 time 对每个节点的 访问时计数，本质是后序遍历的结果 left-right-root
        """
        # 构建邻接表
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for cur, pre in prerequisites:
            adj[pre].append(cur)  # 邻接表出度节点
            indegree[cur] += 1  # 节点入度

        visited = [0] * numCourses  # 0 白色, 1 灰色, 2 黑色; 完全访问完
        finish_t = [0] * numCourses
        invisited = [0] * numCourses  # 节点访问次数

        def dfs(i):  # 节点 idx
            nonlocal time
            if visited[i] == 1:
                return False
            if visited[i] == 2:
                return True

            if indegree[i] > 0:  # 内部点(invisited=indegree), 计算 invisited 数量
                invisited[i] += 1  # 直接加会 漏掉初始节点

            visited[i] = 1  # 灰色

            time += 1
            for j in adj[i]:  # 邻接位置
                if not dfs(j):  # 遍历失败
                    return False
            time += 1

            if invisited[i] == indegree[i]:  # 路径完全走完了
                visited[i] = 2
                finish_t[i] = time
            else:
                visited[i] = 0  # 让这个节点下次 还能遍历

            return True

        select = [True] * numCourses
        res = []

        for i in range(numCourses):
            if indegree[i] == 0:
                time = 0
                if dfs(i):  # 连通分量遍历成功
                    compt_idxs = []
                    for j in range(numCourses):
                        if select[j] and finish_t[j] > 0:
                            compt_idxs.append(j)
                            select[j] = False  # 只选1次

                    res.append(sorted(compt_idxs, key=lambda t: finish_t[t], reverse=True))
                    # t 对应 compt_idxs 每个值

        print(res)
        return res


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

s = Topo()

for num_v, edges in cases:
    # print(s.canFinish(num_v, edges), s.findOrder(num_v, edges))
    s.find_each_Order(num_v, edges)
