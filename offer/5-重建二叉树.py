"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
inorder root_idx 左侧为 左子树，长度 = root_idx
preorder [0] 为 root node，之后长度为 root_idx 为 左子树
"""


class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def build_tree(preorder, inorder):
            assert len(preorder) == len(inorder)

            if len(preorder) > 0:
                root, root_idx = preorder[0], 0  # 最上部根节点
                rootNode = TreeNode(root)

                for idx, val in enumerate(inorder):
                    if val == root:
                        root_idx = idx
                        break

                # 构建左子树
                rootNode.left = build_tree(preorder[1:root_idx + 1], inorder[:root_idx])  # 长度恰为 idx
                # 构建右子树，从 preorder, inorder 截取其 先序，中序
                rootNode.right = build_tree(preorder[root_idx + 1:], inorder[root_idx + 1:])  # 长度恰为 idx

                return rootNode
            else:
                return None

        return build_tree(preorder, inorder)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # 递归建树
        def build_tree(preorder, inorder):
            if len(preorder) > 0:
                root_val, root_idx = preorder[0], 0  # 根节点
                root = TreeNode(root_val)
                # 找到中序中 root 位置
                for idx, val in enumerate(inorder):
                    if root_val == val:
                        root_idx = idx
                        break
                # 使用 root_idx 分割 左右子树，从 preorder 和 inorder 截取子树节点
                root.left = build_tree(preorder[1:root_idx + 1], inorder[:root_idx])
                root.right = build_tree(preorder[root_idx + 1:], inorder[root_idx + 1:])
                return root
            else:
                return None

        return build_tree(preorder, inorder)


preorder = [3, 9, 20, 15, 7]  # 前序遍历
inorder = [9, 3, 15, 20, 7]  # 中序遍历

s = Solution1()
tree = s.buildTree(preorder, inorder)

from base.tree import preOrderTraverse, inOrderTraverse

preOrderTraverse(tree)
print()
inOrderTraverse(tree)
