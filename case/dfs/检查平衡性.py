# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 任意节点 左右子树 高度差 <=1

        def dfs(node: TreeNode):  # 计算平衡树的高度
            if not node:
                return 0
            dleft = dfs(node.left)
            if dleft == -1:
                return -1
            dright = dfs(node.right)
            if dright == -1:
                return -1
            return 1 + max(dleft, dright) if abs(dleft - dright) <= 1 else -1

        return dfs(root) != -1
