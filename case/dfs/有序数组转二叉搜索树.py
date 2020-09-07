from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 有序数组 -> 高度平衡 BST, 左右子树差 <=1
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        # 递归左右子树; 遇到 nums=[] 返回 None
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

    def preorder_traverse(self, root: TreeNode):
        # dfs 先序遍历 root-left-right
        if not root:
            return
        print(root.val, end=',')
        self.preorder_traverse(root.left)
        self.preorder_traverse(root.right)


s = Solution()
tree = s.sortedArrayToBST([-10, -3, 0, 5, 9])
print(s.preorder_traverse(tree))
