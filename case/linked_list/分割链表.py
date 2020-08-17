# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    分割链表:
    以 x 为基准分割链表，使得所有 < x 的节点排在 >= x 的节点之前
    分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间, 不要求结束为 快排终止态
    """

    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None

        # 头插法
        dummy = ListNode(-1)
        dummy.next = head

        p = head
        while p and p.next:
            if p.next.val < x:
                tmp = dummy.next
                dummy.next = p.next  # 将 p.next 插入头部
                p.next = p.next.next  # 跳过 p.next
                dummy.next.next = tmp
            else:
                p = p.next

        return dummy.next

    def partition2(self, head: ListNode, x: int) -> ListNode:
        # 双指针
        # p 左
        # q 右
        p, q = head, head
        while q:
            if q.val < x:  # 发现 < x, 与左方 p 交换值，并且 p,q 继续后移
                q.val, p.val = p.val, q.val
                p = p.next
            q = q.next  # >=x 持续向右
        return head
