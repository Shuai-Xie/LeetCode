"""
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        fast, slow = head, head
        # 快指针的合法性判断很重要, 快指针合法时，慢一定合法
        while fast and fast.next:  # .next 两次，就在这里限定 fast 和 fast.next
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if fast != slow:
            return None
        else:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
