class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 只能访问该节点，其前不可，但其后可
        while node and node.next:
            node.val = node.next.val
            if not node.next.next:  # 是最后1个
                node.next = None
            else:
                node = node.next
