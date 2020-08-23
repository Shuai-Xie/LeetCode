# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        不改变地址，直接修改 left, right 指向
        先序遍历展开
        """

        curnode = root

        def dfs(node:TreeNode):
            if not node:
                return
            dfs(node.)
