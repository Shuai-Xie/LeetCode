class Node:
    def __init__(self, char='', path=0, end=0, next_nodes=[]):
        self.char = char  # 当前节点表示的字符
        self.path = path
        self.end = end
        self.next = {n.char: n for n in next_nodes}  # 后继节点序列


class Trie:
    def __init__(self):
        self.root = Node()

    # 增
    def insert(self, word: str) -> None:
        r = self.root

        for c in word:
            if c not in r.next:
                r.next[c] = Node(char=c)
            r = r.next[c]
            r.path += 1

        r.end += 1

    # 删
    def delete(self, word):
        r = self.root

        for c in word:
            if c not in r.next:  # 直接结束
                return
            if r.next[c].path == 1:  # 经过 c 只有1个节点
                r.next.pop(c)  # 删除此节点，结束
                return
            r = r.next[c]
            r.path -= 1  # word 经过的节点 path-1

        r.end -= 1  # 如果是内部节点，for 中不会停止，这里 end-1=0 除去此 word

    # 查
    def search(self, word: str) -> bool:
        r = self.root

        for c in word:
            if c not in r.next:
                return False
            r = r.next[c]

        return r.end > 0  # 最后一个 char 是 end

    # 前缀判断
    def startsWith(self, prefix: str) -> bool:
        r = self.root

        for c in prefix:
            if c not in r.next:
                return False
            r = r.next[c]

        return True

    # 遍历
    def traverse(self):
        res = {}

        def dfs(node, word=''):
            # preorder 遍历
            word += node.char
            if node.end > 0:
                res[word] = node.end  # word 出现次数
            for n in node.next.values():  # 邻接点
                dfs(n, word)

        dfs(self.root)
        return res


trie = Trie()
trie.insert('12')
trie.insert('123')
trie.insert('1234')
print(trie.traverse())

trie.insert('1234')
trie.insert('1234')
print(trie.traverse())

trie.delete('1234')
print(trie.traverse())

print(trie.start_with('1abc'))
print(trie.search('1abc'))
