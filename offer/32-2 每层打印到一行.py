"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右 保存到一行

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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        vals, depths = [], []

        # DFS 先序遍历, 满足从左到右，depths 是无序的
        def node_depth(node: TreeNode, depth=0):
            if not node:
                return
            depth += 1
            vals.append(node.val)
            depths.append(depth)
            node_depth(node.left, depth)
            node_depth(node.right, depth)

        node_depth(root)

        # 计算得到，每一层的节点的深度；再按行索引
        res = []
        max_d = max(depths)
        for i in range(1, max_d + 1):
            res.append([v for v, d in zip(vals, depths) if d == i])
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        quene = [root]
        while quene:
            # note: 出队列前
            # 当前层 节点全部 出队列，恰好可以得到剩下层的全部节点
            tmp = []
            cur_len = len(quene)  # note: 记录当前长度
            for _ in range(cur_len):
                node = quene.pop(0)  # 头元素 出队列
                if node:
                    tmp.append(node.val)
                    quene.append(node.left)
                    quene.append(node.right)
            if tmp:  # 可能为空, 因为 queue add 的 node 可能为 None
                res.append(tmp)

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
print(s.levelOrder2(a))
