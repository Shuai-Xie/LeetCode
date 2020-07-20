# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 单向链表，长度不可知，无法直接 slice
        # 如果是 双向链表，就可以倒着索引

        # 先遍历完，将倒 k 转成 正数顺位
        p = head
        cnt = 0
        while p:
            cnt += 1
            p = p.next

        m = cnt - k + 1  # 倒数第6，正数第1
        p = head
        cnt = 0
        while p:  # 注意 避免进不了 while 的情况
            cnt += 1
            if cnt == m:
                return p
            p = p.next

    def getKthFromEnd2(self, head: ListNode, k: int) -> ListNode:
        # 快慢指针；快 始终比 慢 快 k 个身位..
        # 循环中，双指针 former 和 latter 每轮都向前走一步; former 到尾部，latter 也就到了
        former, latter = head, head
        for _ in range(k):  # former 先走过 k 步
            former = former.next
        while former:  # former 到结尾，latter 恰好为倒数第 k
            former, latter = former.next, latter.next
        return latter
