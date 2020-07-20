"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 定义两个 指针
        p, q = l1, l2

        top = ListNode(0)
        z = top
        while p and q:  # p,q 都还有元素
            if p.val < q.val:
                z.next = ListNode(p.val)
                p = p.next
            else:
                z.next = ListNode(q.val)
                q = q.next
            z = z.next  # 移到末尾

        # 直接连接上 多余链表 剩下的部分
        # p 和 q 始终在表示 两个子链表的头部
        if p:
            z.next = p
        if q:
            z.next = q

        return top.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 直接使用 l1,l2 而不用 p,q 指代，效率提升很多
        top = ListNode(0)
        z = top
        while l1 and l2:  # p,q 都还有元素
            if l1.val < l2.val:
                z.next = l1
                l1 = l1.next  # l1,l2 始终 在链表的头部
            else:
                z.next = l2
                l2 = l2.next
            z = z.next  # 移到 z 链表末 尾；下轮 while 还会更新 next 指向

        # 直接连接上 多余链表 剩下的部分
        if l1:
            z.next = l1
        if l2:
            z.next = l2

        return top.next
