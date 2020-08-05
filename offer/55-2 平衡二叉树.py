class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 平衡二叉树，任意节点 左右子树深度差 <= 1
    # 推出：树的深度 = 左子树的深度 与 右子树的深度 中的 最大值 +1
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root: TreeNode):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:  # 使用 -1 剪枝，提前返回结果
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            # 满足平衡二叉树，则返回树的深度
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1


from base.tree import build_tree_from_arr

# tree = build_tree_from_arr([3, 9, 20, None, None, 15, 7])
tree = build_tree_from_arr([1, 2, 2, 3, 3, None, None, 4, 4])
s = Solution()
print(s.isBalanced(tree))
