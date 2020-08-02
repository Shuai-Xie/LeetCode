# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 获取二叉树的所有路径 存入 str
        if not root:
            return []
        if not root.left and not root.right:  # 叶节点 path
            return [str(root.val)]  # 对应 List[str]

        paths = []
        for p in self.binaryTreePaths(root.left):  # 头节点 + 子树路径
            paths.append(f'{root.val}->{p}')
        for p in self.binaryTreePaths(root.right):
            paths.append(f'{root.val}->{p}')

        return paths

    def binaryTreePaths_list(self, root: TreeNode) -> List[List[int]]:
        # 获取二叉树的所有路径 存入 list
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]  # 保证 单个元素也返回 List[List[int]]

        paths = []
        for p in self.binaryTreePaths_list(root.left):
            paths.append([root.val] + p)  # 注意后一项要有括号
        for p in self.binaryTreePaths_list(root.right):
            paths.append([root.val] + p)

        return paths
