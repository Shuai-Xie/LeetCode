"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum_slow(self, root: TreeNode, sum: int) -> List[List[int]]:
        def list_sum(arr):
            s = 0
            for v in arr:
                s += v
            return s

        def binaryTreePaths(root: TreeNode) -> List[List[int]]:
            # 获取二叉树的所有路径 存入 list
            if not root:
                return []
            if not root.left and not root.right:
                return [[root.val]]  # 保证 单个元素也返回 List[List[int]]

            paths = []
            for p in binaryTreePaths(root.left):
                paths.append([root.val] + p)  # 注意后一项要有括号
            for p in binaryTreePaths(root.right):
                paths.append([root.val] + p)

            return paths

        paths = binaryTreePaths(root)
        return [p for p in paths if list_sum(p) == sum]

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        先序遍历过程中，记录 root 到当前节点的路径，当路径和为 sum，将路径加入
        note: 从树的根节点开始往下一直到叶节点所经过的节点, 题目限制了 叶节点
        """
        res, path = [], []

        def recur(root, tar):
            # tar: 目标值
            if not root:
                return

            path.append(root.val)
            tar -= root.val  # 更新寻找的路径目标值

            if tar == 0 and not root.left and not root.right:  # 题目限制了是叶节点
                # if tar == 0:  # 假设可以不到叶节点，且节点值>0, pop() 剪枝
                res.append(path[:])  # copy 一份 path，因为后面 path 还要用于 pop 寻找其他解

            recur(root.left, tar)
            recur(root.right, tar)

            path.pop()  # 包含当前 root 的 path 研究完了

        recur(root, sum)

        return res


if __name__ == '__main__':
    from base.tree import build_tree_from_arr, layerTraverse

    s = Solution()

    # tree = build_tree_from_arr([1, 2, 3, 4, 5])
    # print(s.pathSum_slow(tree, 4))
    # print(s.pathSum(tree, 4))

    tree = build_tree_from_arr([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1])
    # print(s.pathSum_slow(tree, 22))
    print(s.pathSum(tree, 22))
    # layerTraverse(tree)
