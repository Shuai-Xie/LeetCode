# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        # 双指针，快慢指针
        p = head
        while k > 0:
            p = p.next
            k -= 1

        q = head
        while p:  # 当 p 为 None，恰与 q 距离 k
            p, q = p.next, q.next
        return q.val
