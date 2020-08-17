# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 相交链表，交点之后，尾部数据相同
        p, q = headA, headB
        # 等长 相交     正向遍历 即得到
        # 不等长 相交   第2次遍历 p=q, 其中1个位None时 另一个不会
        # 不相交        两个都是 None 跳出
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
