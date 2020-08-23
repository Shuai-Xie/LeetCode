class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # dfs 查询树的深度
        def recur(root: TreeNode):
            if not root:
                return 0
            # 左树深度
            dleft = recur(root.left)
            if dleft == -1:
                return -1
            dright = recur(root.right)
            if dright == -1:
                return -1

            return 1 + max(dleft, dright) if abs(dleft - dright) <= 1 else -1

        return recur(root) != -1

    def tree_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.tree_depth(root.left), self.tree_depth(root.right))

    def preorder_traverse(self, root: TreeNode):
        # dfs 先序遍历 root-left-right
        if not root:
            return
        print(root.val, end=',')
        self.preorder_traverse(root.left)
        self.preorder_traverse(root.right)

    def build_tree_from_arr(self, arr) -> TreeNode:
        if not arr:
            return None

        # 先将每个节点值 变为 node
        nodes = [TreeNode(-1)] + [TreeNode(v) for v in arr]

        # 再用 父子 idx 关系，关联树
        n = len(nodes)
        for i in range(1, n):
            if 2 * i < n:
                nodes[i].left = nodes[2 * i]
            else:
                break
            if 2 * i + 1 < n:
                nodes[i].right = nodes[2 * i + 1]
            else:
                break

        return nodes[1]


s = Solution()
tree = s.build_tree_from_arr([1, 2, 3, 4, 5])
s.preorder_traverse(tree)
print()
print(s.tree_depth(tree))
print(s.tree_depth(tree.left), s.tree_depth(tree.right))
