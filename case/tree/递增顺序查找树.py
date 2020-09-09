"""
给你一个树，请你 按中序遍历 重新排列树，
- 使树中最左边的结点现在是树的根，
- 并且每个结点没有左子结点，只有一个右子结点。

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # 中序遍历 + 构建新树
        vals = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)

        inorder(root)

        head = TreeNode(-1)
        p = head
        for v in vals:
            p.right = TreeNode(v)
            p = p.right

        return head.right

    def increasingBST2(self, root: TreeNode) -> TreeNode:
        # 中序过程中，更改树的node, 将左孩子置空，将其本身作为上一个遍历到节点(p) 的右孩子
        # p 记录全局链表的位置
        head = TreeNode(-1)
        p = head

        def inorder(root):
            nonlocal p
            if not root:
                return
            inorder(root.left)
            # 访问到当前 node, 其 left 子树已经全部加到 p 链表中，可置为 None
            root.left = None
            p.right = root
            p = p.right

            inorder(root.right)

        inorder(root)
        return head.right
