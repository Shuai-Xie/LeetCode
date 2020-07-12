"""
链接：https://leetcode-cn.com/problems/course-schedule-ii
现在你总共有 n 门课需要选，记为 0 到 n-1。
在选修某些课程之前需要一些先修课程。 
例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]  先学1再学0

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

输入 课程数 n，先决条件列表 []
输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后

分析
假定某些课程没有先决条件，而某些存在先决条件，则构成的拓扑图或孤立点
因为题目给出的条件为有序对:
- 正常情况：图中不存在孤立点，而构成拓扑排序
- 异常情况：给出的有序对依赖不对，使得课程间依赖图形成循环，这样就无法决定先学习哪个了

提示：根据先决条件列表形成的有序图，判断是否存在循环
- 如果不存在，输出 DFS 或 BFS 学习路径
- 如果存在，不能学完所有课程
"""

"""
对每一个课程进行一次深度遍历， 并用 visited 数组记录每一个课程的访问状态，这样我们可以判断有没有环的存在，如果有环则返回[]
"""


def findOrder(numCourses, prerequisites):
    res = []
    visited = [0] * numCourses
    adjacent = [[] for _ in range(numCourses)]
    # adjacent = [[] * numCourses]  # 巨坑

    # 构建邻接矩阵，每行为 cur 节点先决条件
    for cur, pre in prerequisites:  # 当前点，先决
        adjacent[cur].append(pre)

    def dfs(i):  # 图中节点 i
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True

        visited[i] = 1  # 遍历过 i，置为 1

        # 对每个节点都进行 DFS
        for j in adjacent[i]:
            if not dfs(j):
                return False
        # 如果走完所有邻接点，都没找到已遍历的点，即 visited = 1 的点
        # 说明路径没有环路，状态置为 2，加入 res，下次 DFS 遇到 i，直接返回 True，因为已经保存了其没有环路
        visited[i] = 2

        res.append(i)
        return True

    # DFS 所有节点，如果不存在环路，才返回 res
    for i in range(numCourses):
        if not dfs(i):
            return []

    return res


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(findOrder(numCourses, prerequisites))

# 举个反例
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [2, 1], [1, 3]]  # 后3个形成环路
print(findOrder(numCourses, prerequisites))
