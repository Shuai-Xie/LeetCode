from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

    # 改变相邻2个node指向，将 head 移到末尾
    def reversePrint2(self, head: ListNode) -> List[int]:
        res = []

        if not head:
            return res

        # 相当于 反着 创建了 节点间指针；将链表 head 不断向后传递
        pre = None
        cur, h = head, head

        while cur:
            h = cur  # h 随着 cur 向后遍历
            tmp = cur.next  # 保存 next 下次赋值
            cur.next = pre  # 指向前一个
            # pre/cur 前进
            pre = cur
            cur = tmp

        while h:
            res.append(h.val)
            h = h.next

        return res

    # 头插法
    def reversePrint3(self, head: ListNode) -> List[int]:
        res = []

        if not head:
            return res

        # 头插法
        dummy = ListNode(-1)
        dummy.next = head

        p = head
        while p and p.next:
            tmp = dummy.next
            dummy.next = p.next  # 将 p.next 插入头部
            p.next = p.next.next  # 跳过 p.next, 这里已经在遍历 p.next 了，到 None 时 while 自然结束
            dummy.next.next = tmp

        h = dummy.next
        while h:
            res.append(h.val)
            h = h.next

        return res


# 注意 0 <= 链表长度 <= 10000
def create_listnode(li):
    if li:
        h = ListNode(li[0])  # 保存头节点位置 返回用
        p = h
        for i in range(1, len(li)):
            p.next = ListNode(li[i])
            p = p.next
        return h


def print_listnode(head):
    while head:
        print(head.val, end=', ')
        head = head.next
    print()


li = [1, 3, 2]
head = create_listnode(li)
print_listnode(head)

s = Solution()
# print(s.reversePrint(head))
# print(s.reversePrint2(head))
print(s.reversePrint3(head))
