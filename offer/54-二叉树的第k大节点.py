# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 二叉搜索树的第 k 大节点
    def kthLargest(self, root: TreeNode, k: int) -> int:
        vals = []

        def inorder(node: TreeNode):
            if not node:  # 加了这个 提速很多
                return
            if node.left:  # 先添加 right, 再 left, 可以得到降序序列
                inorder(node.left)
            vals.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)
        return vals[len(vals) - k]


from base.tree import build_tree_from_arr, inOrderTraverse

s = Solution()

# tree = build_tree_from_arr([3, 1, 4, None, 2])
# print(s.kthLargest(tree, 1))
tree = build_tree_from_arr([5, 3, 6, 2, 4, None, None, 1])  # 保证完全二叉树即可
print(s.kthLargest(tree, 3))
