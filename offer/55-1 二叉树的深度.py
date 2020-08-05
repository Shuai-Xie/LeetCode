# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 1+ 拿出 max 后，能减少更多 + 情况，降低时长
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


from base.tree import build_tree_from_arr

tree = build_tree_from_arr([3, 9, 20, None, None, 15, 7])
s = Solution()
print(s.maxDepth(tree))
