"""
通过交换节点的左子节点和右子节点，可以翻转该二叉树中的节点。

从根节点开始的先序遍历报告的 N 值序列。将这一 N 值序列称为树的行程

翻转最少的树中节点，以便树的行程与给定的行程 voyage 相匹配。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    """
    翻转最少的节点 使得 树的先序遍历 与 voyage 给出的 list 一致
        返回 翻转节点值 组成的 list
    """

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        n = len(voyage)  # 节点总数

        flipped = []
        i = 0

        def dfs(node):
            nonlocal i, flipped
            if node:
                if node.val != voyage[i]:  # 节点值 与 不相等?
                    flipped = [-1]
                    return

                i += 1  # 相等情况，继续 dfs 遍历

                if i < n:
                    if node.left and node.left.val != voyage[i]:  # 下一个要遍历的左节点值不等
                        flipped.append(node.val)  # 反转当前节点, 继续向后遍历；因为唯一能使节点相同的方式 就是 翻转节点
                        dfs(node.right)  # 翻转后，先右后左
                        dfs(node.left)
                    else:  # 相等情况，直接 dfs
                        dfs(node.left)
                        dfs(node.right)

        dfs(root)
        return flipped
