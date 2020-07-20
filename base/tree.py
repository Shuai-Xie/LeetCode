class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 构建简单树
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

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
def preOrder(node):
    stack = [node]  # 节点入栈
    while len(stack) > 0:
        node = stack.pop()  # 栈尾元素
        if node:
            print(node.val, end=' ')
            stack.append(node.right)  # 先添加右孩子
            stack.append(node.left)  # 让左孩子先出栈


def inOrder(node):
    stack = []  # 节点入栈
    pos = node
    while pos or len(stack) > 0:
        if pos:  # pos!=None 时，一路添加左孩子
            stack.append(pos)
            pos = pos.left
        else:  # 左孩子到头了
            pos = stack.pop()  # 中
            print(pos.val, end=' ')  # 打印 inOrder 节点
            pos = pos.right  # 遍历右孩子，入栈


def postOrder(node):
    stack = [node]
    stack2 = []
    while len(stack) > 0:
        node = stack.pop()
        stack2.append(node)  # 存储 stack 的依次出栈
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    while len(stack2) > 0:
        print(stack2.pop().val, end=' ')


# 层序遍历
def layerTraverse(node):
    if node is None:
        return None

    queue = [node]

    while len(queue) > 0:
        node = queue.pop(0)  # 出来 queue 首元素
        print(node.val, end=' ')
        # 从左到右，每次可以添加1个节点1层的2个孩子，
        # 而 pop(0) 输出的恰为同层的下一个节点，所以左右孩子也按顺序添加，至此全部添加过程都按顺序
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == '__main__':
    layerTraverse(a)
    # preOrderTraverse(a)
    # print()
    # inOrderTraverse(a)
    # print()
    # postOrderTraverse(a)
