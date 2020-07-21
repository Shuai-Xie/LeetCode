"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # 0 <= 节点个数 <= 1000
        if not root:
            return None

        def mirror(root_: TreeNode):
            if not root_:
                return
            # 自上而下 反转树
            root_.left, root_.right = root_.right, root_.left
            mirror(root_.left)
            mirror(root_.right)

        mirror(root)
        return root
