"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

层序遍历
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        quene = [root]
        while quene:
            node = quene.pop(0)  # 头元素 出队列
            if node:
                res.append(node.val)
                quene.append(node.left)
                quene.append(node.right)

        return res
