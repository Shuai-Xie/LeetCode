# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 每个节点左右两个子树的高度差的绝对值不超过 1
        # 对于 子树高度差 >1 的可以提前剪枝结束

        def recur(root):  # 递归计算 左右子树深度
            if not root:
                return 0

            # 递归计算 左右子树深度
            dleft = recur(root.left)
            if dleft == -1:
                return -1
            dright = recur(root.right)
            if dright == -1:
                return -1

            if abs(dleft - dright) <= 1:
                return 1 + max(dleft, dright)
            else:
                return -1

        return recur(root) != -1
