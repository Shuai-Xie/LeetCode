from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res[::-1]


# 注意 0 <= 链表长度 <= 10000
def cvt_listnode(head):
    h = ListNode(head[0])
    p = h
    for v in head[1:]:
        n = ListNode(v)
        p.next = n
        p = n
    return h


def print_listnode(head):
    while head is not None:
        print(head.val, end=', ')
        head = head.next


head = [1, 3, 2]
head = cvt_listnode(head)
print_listnode(head)

s = Solution()
print(s.reversePrint(head))
