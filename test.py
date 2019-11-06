class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list2listnode(list):
    node = ListNode(list[0])
    p = node
    for i in range(1, len(list)):
        p.next = ListNode(list[i])
        p = p.next
    return node


def traverse(listnode):
    p = listnode
    while p:
        print(p.val, end=',')
        p = p.next


l1 = [5, 2, 3, 4]
l1_node = list2listnode(l1)  # converse list to ListNode
traverse(l1_node)
