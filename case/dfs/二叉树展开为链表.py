# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        寻找前驱节点 空间复杂度 O(1)

        对于当前节点
        - 如果左节点为空，不需操作
        - 如果左节点不为空，那么左子树的最右节点(先序遍历最后1个) 作为右节点的前驱节点

        更新过程中，不是一直维护着顺序；而是每到1个节点，先确保右找到前驱，找到链表部分关系，再继续遍历链表
        """

        cur = root
        while cur:
            # 如果存在左子树，需要为右节点寻找前驱
            if cur.left:
                pre = cur.left
                while pre.right:  # 寻找最右
                    pre = pre.right
                pre.right = cur.right  # 左子树最右 -> cur.right
                cur.right = cur.left  # 右节点 更新链表下一位置
                cur.left = None  # 左节点置为 None

            cur = cur.right  # 链表下一个

    def flatten_store(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        使用外部存储空间，dfs 存储 先序遍历 结果
        再按照结果指针，将右指针作为链表指针
        """

        links = []

        # 递归
        # def dfs(node: TreeNode):
        #     if not node:
        #         return
        #     links.append(node)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)

        # 迭代
        if not root:
            return

        stack = [root]
        while stack:  # 栈内有元素
            root = stack.pop()
            links.append(root)  # 添加栈顶
            if root:
                stack.append(root.right)
                stack.append(root.left)  # 让 left 在栈顶

        n = len(links)

        if n > 1:
            for i in range(n - 1):
                links[i].right = links[i + 1]  # 右指针 = 链表指针
                links[i].left = None  # 左指针 不用
