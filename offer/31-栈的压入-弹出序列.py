"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如，
序列 {1,2,3,4,5} 是某栈的压栈序列，
序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，
但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    """
    借助 辅助栈，根据 pushed 和 popped 序列操作
    模拟 栈的执行 是否正常；循环判断 栈顶元素 == 弹出序列的当前元素
    题目假设压入栈的所有数字均不相等，所以只要满足2行条件，即可出栈
    """

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0  # 使用 stack 作为模拟栈

        for num in pushed:
            stack.append(num)
            # 此刻表示：栈达到任意长度，都可以完全出栈，与 popped 序列比较
            while stack and stack[-1] == popped[i]:  # 栈顶元素 == 弹出序列的当前元素
                stack.pop()  # 模拟出栈
                i += 1  # 判断下一元素
            # stack 出栈到 poped 序列不等时，之后可继续压栈，再与 poped 剩下出栈顺序比较

        return not stack  # 如果栈能完全出完，满足
