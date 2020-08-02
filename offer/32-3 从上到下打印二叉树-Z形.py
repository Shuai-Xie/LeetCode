"""
请实现一个函数按照 "之字形"顺序 打印二叉树，
第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，
第三行再按照从左到右的顺序打印，其他行以此类推
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        quene = [root]
        odd_flag = True  # 奇数层
        while quene:
            # 当前层 节点全部 出队列，恰好可以得到剩下层的全部节点
            tmp = []
            cur_len = len(quene)  # note: 记录当前长度

            # 出栈顺序不变，只要反转序列即可
            for _ in range(cur_len):
                node = quene.pop(0)  # 头元素 出队列
                if node:
                    tmp.append(node.val)
                    quene.append(node.left)
                    quene.append(node.right)

            if tmp:  # 可能为空, 因为 queue add 的 node 可能为 None
                res.append(tmp if odd_flag else tmp[::-1])

            odd_flag = not odd_flag

        return res


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

s = Solution()
print(s.levelOrder(a))
