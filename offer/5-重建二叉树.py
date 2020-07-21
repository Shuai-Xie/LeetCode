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
先序 + 中序 重建二叉树
后序 + 中序
inorder root_idx 左侧为 左子树，【长度 = root_idx】关键
preorder[0]   为 root node，之后长度为 root_idx 为 左子树；再往后到末尾为右子树
postorder[-1] 为 root node，从 0 开始长度为 root_idx 为 左子树；其后到 -1 为右子树
"""


class Solution:
    # 先序 + 中序
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder and inorder and len(preorder) == len(inorder):
            root_val, root_idx = preorder[0], 0
            root = TreeNode(root_val)
            # 在 inorder 中寻找 root 位置；切分
            for idx, val in enumerate(inorder):
                if val == root_val:
                    root_idx = idx
                    break
            # 找到中序中 root_idx；切分左右子树
            root.left = self.buildTree(preorder[1:root_idx + 1], inorder[:root_idx])
            root.right = self.buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])

            return root  # 递归返回最上层的 root

    # 后序 + 中序
    def buildTree_post(self, postorder: List[int], inorder: List[int]) -> TreeNode:
        if postorder and inorder and len(postorder) == len(inorder):
            root_val, root_idx = postorder[-1], len(postorder) - 1
            root = TreeNode(root_val)

            # 寻找 inorder 中 root 位置
            for idx, val in enumerate(inorder):
                if val == root_val:
                    root_idx = idx
                    break

            # 构建左右子树; 中序遍历中 root_idx 位置 == 左子树的长度
            root.left = self.buildTree_post(postorder[:root_idx], inorder[:root_idx])
            root.right = self.buildTree_post(postorder[root_idx:-1], inorder[root_idx + 1:])

            return root


from base.tree import preOrderTraverse, inOrderTraverse, postOrderTraverse, build_tree_from_arr


def rebuild_tree():
    preorder = [3, 9, 20, 15, 7]  # 前序遍历
    inorder = [9, 3, 15, 20, 7]  # 中序遍历
    postorder = [9, 15, 7, 20, 3]  # 后序遍历

    s = Solution()

    # 先序 创建
    tree = s.buildTree(preorder, inorder)

    preOrderTraverse(tree)
    print()
    inOrderTraverse(tree)
    print()
    postOrderTraverse(tree)
    print()

    # 后序 创建
    tree = s.buildTree_post(postorder, inorder)

    preOrderTraverse(tree)
    print()
    inOrderTraverse(tree)
    print()
    postOrderTraverse(tree)
    print()


if __name__ == '__main__':
    # 有 先序/后序 + 中序 重新创建树
    # rebuild_tree()
    tree = build_tree_from_arr(arr=[3, 9, 20, None, None, 15, 7])
    preOrderTraverse(tree)
    print()
    inOrderTraverse(tree)
    print()
    postOrderTraverse(tree)
    print()
