class Node:
    def __init__(self, val=None, path=0, end=0, next_nodes=[]):
        """
        :param val: 当前节点的值，对应 c
        :param path: 有多少条 path 经过了当前节点，delete word 时需要判断 从哪里开始删除
        :param end: 有多少 word 以当前节点为末节点，用来判断 word 是否存在
        :param next_nodes: 当前节点的 后继孩子，dict, key 各不相同
            字典树由来：孩子的值 作为字典的 key，查找为 O(1)，所以比平衡树 O(mlog(n)) 好
        """
        self.val = val
        self.path = 0
        self.end = 0
        self.next = {node.val: node for node in next_nodes}  # dict {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(val='')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        每个插入1个相同 word，那么路径上的 node 的 path/end 都会+1
        """
        r = self.root
        for c in word:
            if c not in r.next:
                r.next[c] = Node(c)  # 添加新的子 node
            r = r.next[c]  # 遍历已有 node
            r.path += 1  # 经过 r 的 path+1

        r.end += 1  # 以 r 为 end 的 word+1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        r = self.root

        for c in word:
            if c not in r.next:
                return False
            r = r.next[c]

        return r.end > 0

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        r = self.root

        for c in prefix:
            if c not in r.next:
                return False
            r = r.next[c]

        return True

    def traverse(self):
        """
        返回所有 存入的 str
        """
        res = {}  # word:num

        def dfs(node: Node, word=''):  # 能传入的必然不为 None
            word += node.val  # 将 root.val = '', 就不用判断是否为首节点
            if node.end > 0:
                res[word] = node.end  # 记录每个 word 个数
            # 添加后 仍然能继续向后遍历
            for n in node.next.values():  # 传入 node
                dfs(n, word)

        dfs(self.root)
        return res

    def delete(self, word: str) -> None:
        """
        两种情况: 内部节点, 叶子节点

        """
        r = self.root

        for c in word:
            if c not in r.next:  # 不存在，直接
                return
            if r.next[c].path == 1:  # 经过的路径只有1条; 寻找到第1个 path=1 节点，删去
                r.next.pop(c)
                return
            r = r.next[c]  # 叶子路径
            r.path -= 1  # 同时更新通过 c 的 path 数量

        r.end -= 1  # 内部，所有节点 path>1, 通过将 end-1=0 去掉这个 word


trie = Trie()
trie.insert('12')
trie.insert('13')
trie.insert('14')
trie.insert('123')
trie.insert('1234')

trie.delete('1234')
print(trie.traverse())

trie.insert('1234')
trie.insert('1234')
trie.insert('123')
print(trie.traverse())
