class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        除了常规操作 还支持返回 最小值
        """
        self.arr = []

    def push(self, x: int) -> None:
        if not self.arr:
            self.arr.append((x, x))  # 元素, min
        else:
            self.arr.append((x, min(x, self.arr[-1][1])))  # 顺序添加，栈顶元素始终包含着当前状态下的 min, 有点 dp 味道, 只与上一时刻 min 有关

    def pop(self) -> None:
        if self.arr:
            self.arr.pop()

    def top(self) -> int:
        if self.arr:
            return self.arr[-1][0]

    def getMin(self) -> int:
        if self.arr:
            return self.arr[-1][1]
