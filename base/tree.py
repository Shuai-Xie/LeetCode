class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
二叉树的 三序遍历 真是递归完美的展现
无论哪种遍历 都要先定义好递归出口
"""


# 先序：根节点->左子树->右子树
# 1 2 4 5 3 6 7
def preOrderTraverse_return(node):
    res = []

    def dfs(node):
        if node:
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

    dfs(node)
    return res


# 先序：根节点->左子树->右子树
# 1 2 4 5 3 6 7
def preOrderTraverse(node):
    if not node:
        return
    print(node.val, end=' ')
    preOrderTraverse(node.left)
    preOrderTraverse(node.right)


# 中序：左子树->根节点->右子树
# 4 2 5 1 6 3 7 每个树节点都投影到地平线
def inOrderTraverse(node):
    if node is None:
        return
    inOrderTraverse(node.left)
    print(node.val, end=' ')
    inOrderTraverse(node.right)


# 后序：左子树->右子树->根节点
# 4 5 2 6 7 3 1 先左右，再出根
def postOrderTraverse(node):
    if node is None:
        return
    postOrderTraverse(node.left)
    postOrderTraverse(node.right)
    print(node.val, end=' ')


def preOrderStack(node):
    res = []
    stack = [node]
    while stack:
        node = stack.pop()  # -1
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)  # 放后 先出栈
    return res


def inorderStack(node):
    res = []
    stack = []
    while node or stack:
        if node:
            stack.append(node)  # 左节点入栈
            node = node.left
        else:
            node = stack.pop()  # 为空弹出，遍历右节点
            res.append(node.val)
            node = node.right  # 判断右路


def postOrderStack(node):
    res = []
    stack = [node]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

    return res[::-1]


def layerTraverse(node):
    res = []
    quene = [node]
    while quene:
        node = quene.pop(0)
        if node:
            res.append(node.val)
            quene.append(node.left)  # 先进先出
            quene.append(node.right)
    return res


def build_tree_from_arr(arr):
    """
    根据完全二叉树 父子节点 与 arr idx 之间关系
    """
    if not arr:
        return None

    # 节点从 1 开始
    nodes = [None] + [TreeNode(v) if v else None for v in arr]

    num = len(nodes)
    for i in range(1, num):
        if nodes[i]:  # 判断 node 是否为 None
            if 2 * i < num:
                nodes[i].left = nodes[2 * i]
            if 2 * i + 1 < num:
                nodes[i].right = nodes[2 * i + 1]

    return nodes[1]  # 首节点


from typing import List


def binaryTreePaths_str(root: TreeNode) -> List[str]:
    # 获取二叉树的所有路径 存入 str
    if not root:
        return []
    if not root.left and not root.right:
        return [str(root.val)]

    paths = []
    for p in binaryTreePaths_str(root.left):  # 头节点 + 子树路径
        paths.append(f'{root.val}->{p}')
    for p in binaryTreePaths_str(root.right):
        paths.append(f'{root.val}->{p}')

    return paths


def binaryTreePaths(root: TreeNode) -> List[List[int]]:
    # 获取二叉树的所有路径 存入 list
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]

    paths = []
    for p in binaryTreePaths(root.left):
        paths.append([root.val] + ([p] if not isinstance(p, list) else p))  # 注意后一项要有括号
    for p in binaryTreePaths(root.right):
        paths.append([root.val] + ([p] if not isinstance(p, list) else p))

    return paths


if __name__ == '__main__':
    a = build_tree_from_arr([1, 2, 3, 4, 5, 6, 7])
    # a = build_tree_from_arr([1, 2, 3, 4])
    # print(binaryTreePaths(a))
    # print(binaryTreePaths_str(a))

    print(layerTraverse(a))
    print(preOrderTraverse(a))
    print(preOrderStack(a))

    # inOrderTraverse(a)
    # print()
    # inOrderStack(a)
    # print()

    # postOrderTraverse(a)
    # print()
    # postOrderStack(a)
    # print()
