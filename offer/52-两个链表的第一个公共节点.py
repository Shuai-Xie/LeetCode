"""
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 两个链表的 公共节点，先反向，再判断
    # 不能只根据 链表的值 判断反向是否分叉，存在分叉点之后，值依然相等情况
    # 考察链表 可能本质在 考察指针
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            # 遍历到末尾后，换用另一个, 这样二者到交叉点走过的距离就相等了
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
