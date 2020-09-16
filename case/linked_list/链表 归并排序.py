class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeSort(self, head: ListNode) -> ListNode:
        def get_mid(h: ListNode):  # head
            # 快慢 指针 找到 1/2 位置
            if not h or not h.next:
                return h

            # fast = 2*slow, fast 到达末尾时，slow 恰好在中间
            slow, fast = h, h.next
            while fast and fast.next:  # 跳出位置, 偶数 fast.next 为空，奇数 fast.next.next 为空
                fast = fast.next.next
                slow = slow.next
            return slow

        def merge_two_lists(l1, l2):
            dummy = p = ListNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next  # p 总是要向后遍历
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return dummy.next

        if not head or not head.next:
            return head

        # 中点切割左右链
        mid = get_mid(head)  # 快慢指针

        right, mid.next = mid.next, None  # 右链, 左链 head 出发，末尾置为 None
        return merge_two_lists(self.mergeSort(head), self.mergeSort(right))

    def traverse(self, head: ListNode):
        while head:
            print(head.val, end=',')
            head = head.next
        print()

    def create_linkedlist_from_arr(self, arr):
        if arr:
            dummy = ListNode(-1)
            p = ListNode(arr[0])
            dummy.next = p  # 起到记录链表初始位置作用
            for i in range(1, len(arr)):
                p.next = ListNode(arr[i])
                p = p.next
            return dummy.next


s = Solution()
head = s.create_linkedlist_from_arr([3, 5, 8, 5, 10, 2, 1])
s.traverse(head)

h = s.mergeSort(head)
s.traverse(h)
