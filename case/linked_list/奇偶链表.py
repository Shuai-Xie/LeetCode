class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 奇数位 - 偶数位 分开
        if not head or not head.next:
            return head

        odd, even = head, head.next
        even_head = even  # 需要这个中间变量，因为 head.next 指向已经改变了

        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
