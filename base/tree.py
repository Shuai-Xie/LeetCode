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
def preOrderTraverse(node):
    if not node:
        return None
    print(node.val, end=' ')
    preOrderTraverse(node.left)
    preOrderTraverse(node.right)


# 中序：左子树->根节点->右子树
# 4 2 5 1 6 3 7 每个树节点都投影到地平线
def inOrderTraverse(node):
    if node is None:
        return None
    inOrderTraverse(node.left)
    print(node.val, end=' ')
    inOrderTraverse(node.right)


# 后序：左子树->右子树->根节点
# 4 5 2 6 7 3 1 先左右，再出根
def postOrderTraverse(node):
    if node is None:
        return None
    postOrderTraverse(node.left)
    postOrderTraverse(node.right)
    print(node.val, end=' ')


# 非递归
# 用栈模拟 递归的过程
# 根-左-右
def preOrderStack(node):
    if not node:
        return None

    stack = [node]  # 节点入栈
    while stack:
        node = stack.pop()  # 栈尾元素, -1
        if node:
            print(node.val, end=' ')
            stack.append(node.right)  # 先添加右孩子
            stack.append(node.left)  # 让左孩子先出栈
            # 先出栈的放在栈顶


def inOrderStack(node):
    if not node:
        return None

    stack = []
    while node or stack:  # node 对应 if, stack 对应 else
        if node:  # 首节点, 方便根据 node 压入节点
            stack.append(node)
            node = node.left  # 将左节点不断压栈
        else:  # 当左节点为空时，出栈当前节点，并进入右节点
            node = stack.pop()
            print(node.val, end=' ')
            node = node.right


def postOrderStack(node):
    if not node:
        return None

    stack = [node]
    stack2 = []

    while stack:
        node = stack.pop()
        if node:
            stack2.append(node.val)  # 存储 stack 的依次出栈
            stack.append(node.left)  # stack 先压 left 再 right，出栈时对于 stack2，先压 right 再 left；那么 stack2 出栈 就是 left-right-root
            stack.append(node.right)
            # 与 preOrderStack 对比
            # 在 pre 中，node.val 直接 print
            # 而 post 使用 stack2 将 root 压入栈底

    while stack2:  # 出栈顺序
        print(stack2.pop(), end=' ')


# 层序遍历
def layerTraverse(node):
    if node is None:
        return None

    queue = [node]

    while queue:
        node = queue.pop(0)  # 出来 queue 首元素
        if node:
            print(node.val, end=' ')
            queue.append(node.left)
            queue.append(node.right)


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
    # a = build_tree_from_arr([1, 2, 3, 4, 5, 6, 7])
    a = build_tree_from_arr([1, 2, 3, 4])
    print(binaryTreePaths(a))
    print(binaryTreePaths_str(a))

    # layerTraverse(a)
    # print()

    # preOrderTraverse(a)
    # print()
    # preOrderStack(a)
    # print()

    # inOrderTraverse(a)
    # print()
    # inOrderStack(a)
    # print()

    # postOrderTraverse(a)
    # print()
    # postOrderStack(a)
    # print()
