# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 链表反转
        # 0 <= 节点个数 <= 5000; 小心 0个节点的 问题
        if not head:
            return None

        vals = []
        p = head
        while p:
            vals.append(p.val)
            p = p.next
        vals = vals[::-1]  # 反转值

        head.val = vals[0]
        p = head
        for v in vals[1:]:
            p.next = ListNode(v)
            p = p.next  # 别忘了指向下一个
        return head

    def reverseList2(self, head: ListNode) -> ListNode:
        """
        使用 哑节点，头插法，有点像插入排序
        """
        if not head:
            return None

        top = ListNode(0)
        top.next = ListNode(head.val)  # 插入头节点?

        p = head.next
        while p:
            q = ListNode(p.val)
            q.next = top.next  # 先让新节点 拿到 原始 top.next; 后面的不会断
            top.next = q  # 再更新 top.next 为新节点

            # 遍历链表
            p = p.next
        return top.next
