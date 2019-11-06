"""2.两数相加
https://leetcode-cn.com/problems/add-two-numbers/
https://leetcode-cn.com/problems/add-two-numbers/solution/liang-shu-xiang-jia-by-leetcode/

- 链表初始化、遍历
- 哑结点来简化代码，哑结点就是没有赋有效值的头结点
- 使用进位 carry 简化问题
- 活用 p, p.next，往往 while p: p = p.next
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def init_ListNode(list):
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


class SolutionNode:
    def addTwoNumbers(self, l1, l2):  # l1, l2 is ListNode
        dummy_head = ListNode(0)  # 哑结点简化代码
        p, q, cur = l1, l2, dummy_head
        carry = 0  # 进位
        while p or q:  # or 可以计算完!
            x = p.val if p else 0  # 完美解决其中1个list到头的问题
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum // 10  # 更新进位，其实对于加法 carry = 1
            cur.next = ListNode(sum % 10)  # 这里是在给 l3 赋值
            cur = cur.next
            if p:  # 如果 p 是最后1个，那么 p.next=None,下一轮 while, p.val=0
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dummy_head.next


class SolutionList:
    def addTwoNumbers(self, l1, l2):
        """
        仿照 ListNode 思想，使用 carry 存储进位，不会改变 l1, l2 的值
        """
        l3 = []
        carry = 0
        for i in range(max(len(l1), len(l2))):
            x = l1[i] if i < len(l1) else 0
            y = l2[i] if i < len(l2) else 0
            sum = x + y + carry
            carry = sum // 10
            l3.append(sum % 10)
        if carry > 0:
            l3.append(carry)

        return l3

    def addTwoNumbers2(self, l1, l2):
        """
        先调整 l1,l2 为等长，再在 l2 进位，会改变 l2 的值
        """
        diff_len = len(l1) - len(l2)
        if diff_len > 0:
            l2.extend([0 for _ in range(diff_len)])
        elif diff_len < 0:
            l1.extend([0 for _ in range(-diff_len)])

        l3 = []
        for i in range(len(l1)):
            tmp = l1[i] + l2[i]
            if tmp < 10:
                l3.append(tmp)
            else:
                l3.append(tmp - 10)
                if i < len(l1) - 1:
                    l2[i + 1] += 1  # 下一位数进1
                else:  # 如果已到最后一位，仍要进1
                    l3.append(1)

        return l3


l1 = [5, 2, 3, 4]
l2 = [6, 7, 6, 6]
l1_node = init_ListNode(l1)  # converse list to ListNode
l2_node = init_ListNode(l2)
print(SolutionList().addTwoNumbers(l1, l2))
print(SolutionList().addTwoNumbers2(l1, l2))

l3_node = SolutionNode().addTwoNumbers(l1_node, l2_node)
traverse(l3_node)
