"""
请实现 copyRandomList 函数，复制一个复杂链表。
在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):  # 'Node' 也表示属于自定义 Node 类型
        self.val = int(x)
        self.next = next
        self.random = random  # 指向链表 任意节点; 额外的存储空间 充分利用


# a = Node(2)
# print(type(a.next))  # <class 'NoneType'>
# print(a.next)  # None
# print(type(None))


class Solution:
    """
    难点：复制之后，不易记录 next, random 指向的位置；从 hashmap 存储对应关系
    注意是 链表的复制，需要重新初始化节点，而不是改变指针就行了
    """

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None

        node_dict = {}

        p = head
        while p:  # 单向链表 复制节点值
            node_dict[p] = Node(p.val)  # 将 p 中每个 node 与 copyList 中 node 对应
            p = p.next
        p = head
        while p:  # 赋值节点指向；注意 node_dict 的 key 是不为 None 的，而 p.next, random 指向却可能是 None
            node_dict[p].next = node_dict.get(p.next)  # get() 更安全，获取不到为 None
            node_dict[p].random = node_dict.get(p.random)
            p = p.next

        return node_dict[head]
