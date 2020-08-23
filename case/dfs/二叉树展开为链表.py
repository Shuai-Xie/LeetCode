# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        寻找前驱节点
        空间复杂度 O(1)
        """

        pass

    def flatten_store(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        使用外部存储空间，dfs 存储 先序遍历 结果
        再按照结果指针，将右指针作为链表指针
        """

        links = []

        # 递归
        # def dfs(node: TreeNode):
        #     if not node:
        #         return
        #     links.append(node)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)

        # 迭代
        if not root:
            return

        stack = [root]
        while stack:  # 栈内有元素
            root = stack.pop()
            links.append(root)  # 添加栈顶
            if root:
                stack.append(root.right)
                stack.append(root.left)  # 让 left 在栈顶

        n = len(links)

        if n > 1:
            for i in range(n - 1):
                links[i].right = links[i + 1]  # 右指针 = 链表指针
                links[i].left = None  # 左指针 不用
