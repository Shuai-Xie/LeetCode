# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        """
        删除链表中值为 val 的 node
        :param head:
        :param val:
        :return:
        """
        # 如果 head 即为要删除的值
        if head.val == val:
            return head.next
        else:
            p = head
            while p.next:  # 判断下个元素是否为 val，是 就指向下下
                if p.next.val == val:
                    p.next = p.next.next
                    break
                p = p.next  # 别忘了向后遍历
            return head
