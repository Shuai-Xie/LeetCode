"""
数量最多的那种颜色的所有苹果
"""


class TreeNode:
    def __init__(self, val, color, children):
        self.val = val  # 节点id
        self.color = color  # 节点颜色
        self.children = children  # 邻接点

    # def __str__(self):
    #     return 'id: {}, color: {}, children: {}'.format(
    #         self.val, self.color, [t.val for t in self.children]
    #     )


# 节点个数
n = int(input())

# 第i条边连接的两个节点
edges = []
for _ in range(n - 1):
    edges.append(tuple(map(int, input().split())))  # 相连节点的 id

# 节点颜色
colors = list(map(int, input().split()))

# 查询次数
q = int(input())
# 添加查询节点 id
query = []
for _ in range(q):
    query.append(int(input()))

# n = 7
# edges = [
#     (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)
# ]
# colors = [1, 1, 2, 1, 2, 2, 3]
# query = [1, 2, 3, 4, 5, 6, 7]

# 先构建所有节点
nodes = []
for i in range(n):
    nodes.append(TreeNode(i + 1, colors[i], []))  # i+1 节点id

# 再根据 edges 建立连接关系
for u, v in edges:
    nodes[u - 1].children.append(nodes[v - 1])


def get_max_color(node_id):
    color_cnt = {}
    begin_node = nodes[node_id - 1]

    def dfs(node: TreeNode):
        color_cnt[node.color] = color_cnt.get(node.color, 0) + 1
        for child in node.children:
            dfs(child)

    dfs(begin_node)
    max_c = max(color_cnt.values())
    return min([c for c, v in color_cnt.items() if v == max_c])


for t in query:
    print(get_max_color(t))
