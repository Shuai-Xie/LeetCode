"""
输入一个整数数组，判断该数组是不是 某二叉搜索树的后序遍历 结果。
如果是则返回 true，否则返回 false。
假设输入的数组的任意两个数字都互不相同。
"""

from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """
        note: 二叉搜索树，满足大小关系
        递归判断 子问题(子树) 满足 左 < 中 < 右；从 root 判断到 leaf 逐渐向下
        只有 leaf 子问题也满足，包含其的子树才能满足
        """

        def recur(i, j):
            """
            i,j: 后序序列 左右 idx
            postorder[j] 即子树的根节点
            """
            if i >= j:  # 子树节点数量 <=1，上层子树都已满足 左 < 中 < 右; 左右内部的下层子树 递归向下判断 直到节点判完
                return True

            # 寻找左侧第一个 > root 的值所在位置，能切分左右子树
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p  # 保存切分位置

            # 从第一个 > root 的值开始，向右继续找 > root 的值，若 = root 时 恰好到 j，满足
            while postorder[p] > postorder[j]:
                p += 1

            # p==j 判断：右子树的所有节点 都 > root
            # 在寻找 m 的时候，已经满足 左子树所有节点都 < root
            # 递归 精细判断 子树
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
