"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

DFS 返回子树遍历列表；如果和B深度遍历一样，就返回 True
"""

from typing import List
from functools import reduce


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, arrs) -> TreeNode:  # 完全二叉树，root 和 child 位置有关系；但这里用不上
        if len(arrs) == 0:
            return None

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        两个过程
        1. DFS 遍历 A 的所有子节点，得到其 子树
        2. DFS 同时遍历 A 子树 和 B，要求其 value 必须满足包含关系
        """
        if not A or not B:  # 任意一个为 空树；递归的子树 比较也满足
            return False

        def compare(A: TreeNode, B: TreeNode):
            """
            DFS 先序遍历，递归比较 A,B 两个子树
            假设 A 此时为 A 的子树节点；与 B 同时先序遍历，比较二者
            """
            # 定义2个递归出口

            # B 作为 A 的子树；可以存在 某个节点空缺，而 A 却包含的情况
            if not B:  # B 先比对完，才返回 True; 如果 A 先完，说明 B 比当前子树长
                return True

            # B 还有，而 A 已空, False;
            # B,A 的 root 节点值不同, False
            if not A or A.val != B.val:
                return False

            # 根节点值 相等后，再比较左右子树
            return compare(A.left, B.left) and compare(A.right, B.right)

        # compare 在首位，DFS 先序遍历，先判断根节点
        return compare(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isSubStructure_False(self, A: TreeNode, B: TreeNode) -> bool:
        """
        太片面；树拉成 1D 后；中间相同的片段，不代表其在树上的结构也相同
        """
        # 节点个数：[0,10000]
        if not A or not B:  # 任意一个为 空树
            return False

        # 外部传入 paths，即可保存路径
        def bfs(root: TreeNode, paths: List):  # 中序遍历; 左中右
            # 先定义递归出口
            if not root:
                return
            # 左，中，右
            bfs(root.left, paths)  # 不需要判断 None，递归下一层会判断
            paths.append(root.val)
            bfs(root.right, paths)

        # 得到 B 的 path
        a_paths, b_paths = [], []
        bfs(A, a_paths)
        bfs(B, b_paths)

        # a_paths = reduce(lambda x, y: x + y, )
        # b_paths = reduce(lambda x, y: x + y, map(str, b_paths))

        a_paths = ''.join(map(str, a_paths))
        b_paths = ''.join(map(str, b_paths))

        return b_paths in a_paths


a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(2)
a.left = b
a.right = c
b.left = d
b.right = e

b = TreeNode(4)
b.left = TreeNode(1)

s = Solution()
print(s.isSubStructure(a, b))
