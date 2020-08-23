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
            # 使用了新空间，也可以考虑 不用新空间
            q = ListNode(p.val)
            q.next = top.next  # 先让新节点 拿到 原始 top.next; 后面的不会断
            top.next = q  # 再更新 top.next 为新节点

            # 遍历链表
            p = p.next
        return top.next

    def reverseList3(self, head: ListNode) -> ListNode:
        if not head:
            return None

        # 使用 pre,cur 转换指向
        pre, cur = None, head
        h = head  # h 的作用 其实是 记录 cur 的上一个位置，当 cur=None 可以跳出

        while cur:  # cur 为 None 表示到末尾了
            h = cur  # 不断赋值 cur.next
            tmp = cur.next  # 保存 cur 的下一个，用于向后遍历
            cur.next = pre  # 指向前一个
            pre = cur  # 二者 都去往下一个
            cur = tmp

        return h

    def create_list_from_arr(self, arr):
        head = ListNode(arr[0])
        h = head  # h 向后遍历
        for i in range(1, len(arr)):
            h.next = ListNode(arr[i])
            h = h.next
        return head

    def traverse(self, head):
        while head:
            print(head.val, end=',')
            head = head.next
        print()


if __name__ == '__main__':
    s = Solution()
    head = s.create_list_from_arr([1, 2, 3, 4])
    s.traverse(head)
    # h = s.reverseList2(head)
    h = s.reverseList3(head)
    s.traverse(h)
