"""2.两数相加
https://leetcode-cn.com/problems/add-two-numbers/
https://leetcode-cn.com/problems/add-two-numbers/solution/liang-shu-xiang-jia-by-leetcode/

- 链表初始化、遍历
- 哑结点来简化代码，哑结点就是没有赋有效值的头结点
- 使用进位 carry 简化问题
- 活用 p, p.next，往往 while p: p = p.next
"""


# Definition for singly-linked list. 单向链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def init_ListNode(list):
    # 从 list 的 第1个元素开始 初始化链表
    node = ListNode(list[0])
    p = node
    for i in range(1, len(list)):
        p.next = ListNode(list[i])
        p = p.next
    return node


def traverse(listnode):
    p = listnode
    while p:
        if p.next is None:  # 最后1个值
            print(p.val)
        else:
            print(p.val, end=',')
        p = p.next


def addTwoNumbers(l1, l2):  # l1, l2 is ListNode
    # set dummy head for sum linked list
    dummy_head = ListNode(0)  # 哑结点简化代码
    p, q, cur = l1, l2, dummy_head  # l1,l2 本身没有 dummy head
    carry = 0  # 进位 简化加法的过程
    while p or q:  # or 将2个链表都遍历完
        x = p.val if p else 0  # 完美解决其中1个list到头的问题，相当于在 list 左边位置赋 0
        y = q.val if q else 0
        sum = x + y + carry
        carry = sum // 10  # 更新进位，其实对于加法 carry = 1
        cur.next = ListNode(sum % 10)  # 这里是在给 l3 赋值
        cur = cur.next
        if p:  # 如果 p 是最后1个，那么 p.next=None,下一轮 while, p.val=0
            p = p.next
        if q:
            q = q.next
    if carry > 0:  # 遍历完后，判断最左侧是否还要加1
        cur.next = ListNode(carry)
    return dummy_head.next  # 从 sum 的最后1位开始


l1 = [5, 2, 3, 4]
l2 = [6, 7, 6, 6]
l1_node = init_ListNode(l1)  # converse list to ListNode
l2_node = init_ListNode(l2)

l3_node = addTwoNumbers(l1_node, l2_node)
traverse(l3_node)
