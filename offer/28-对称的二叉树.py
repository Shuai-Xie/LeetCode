"""
请实现一个函数，用来判断一棵二叉树是不是对称的。
如果一棵二叉树和它的镜像一样，那么它是对称的。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 0 <= 节点个数 <= 1000 空树也对称
        def compare(L: TreeNode, R: TreeNode):
            if not L and not R:
                return True  # 二者都到头
            if not L or not R or L.val != R.val:
                return False  # 对比失败

            # 对比 root 对称后，比较二者子树 是否对称
            # 形象化：把 树两边的 节点比较完之后，再慢慢朝内
            return compare(L.left, R.right) and compare(L.right, R.left)

        return compare(root.left, root.right) if root else True  # 空树也对称
