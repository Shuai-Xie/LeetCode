"""
深度优先一般用递归，广度优先一般用队列。
一般情况下能用递归实现的算法大部分也能用堆栈来实现。
"""


def bfs(graph, start):
    queue = [start]
    visited = {}  # python 3.6 字典默认 key 有序; O(1) 查找, 使用 set 会导致最后无序输出

    while queue:
        u = queue.pop(0)
        visited[u] = None
        for v in graph[u]:
            if v not in visited:
                queue.append(v)

    return list(visited.keys())


def dfs(graph, start):
    stack = [start]
    visited = {}

    while stack:
        u = stack.pop()  # 栈顶元素 总是目前访问最深的; 然后继续探索更深的
        visited[u] = None
        for v in graph[u]:
            if v not in visited:
                stack.append(v)

    return list(visited.keys())


G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# G = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': [],
#     'D': [],
#     'E': []
# }

print(bfs(G, 'A'))
print(dfs(G, 'A'))
