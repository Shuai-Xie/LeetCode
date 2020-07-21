"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)。
"""


class MinStack:

    def __init__(self):
        """
        借助辅助栈，使得 min 操作由 O(N) 降到 O(1)
        """
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        # A 加入 x 之前的最小值 > x；B 中添加新的最小值
        # 只有初始 A 为空的时候，B 也为空；之后 只有 A 全部 pop，B 才为空
        # B 中元素 始终表示 x 添加前 A 中的当前的最小值；随着 x 添加的不同时刻，而增加为不同时刻的 min
        if not self.B or self.B[-1] >= x:  # 注意：非严格降序 体现在 >=，因为 A 每次只 pop 一个，如果出现重复 min，B 也必须添加进去
            self.B.append(x)  # 新的最小元素添加到栈顶

    def pop(self) -> None:
        # .pop 时 元素已经出栈了
        # 栈顶 恰为 min，B 也 pop
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    # top 和 min 完美对称
    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]  # B 栈顶元素 为min
