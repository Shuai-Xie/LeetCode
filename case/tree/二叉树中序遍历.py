# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            if root.left:
                inorder(root.left)
            # 中序
            res.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)
        return res

    def inorderTraversal_iter(self, root: TreeNode) -> List[int]:
        # 迭代法
        res = []
        stack = []

        while root or stack:
            if root:
                stack.append(root)  # 根节点先压栈
                root = root.left  # 完成左节点的深度遍历压栈
            else:  # 遍历到头了
                root = stack.pop()  # 弹出
                res.append(root.val)
                root = root.right  # 判断右侧

        return res

    def preorderTraversal_iter(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]

        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.append(root.right)
                stack.append(root.left)

        return res

    def postorderTraversal_iter(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]

        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)  # 根先入栈
                stack.append(root.left)  # left 先入 stack，后出栈，后入 stack2, 先出 stack2
                stack.append(root.right)

        return res[::-1]
