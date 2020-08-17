class TripleInOne:
    """
    只用1个数组 实现三个栈
    """

    def __init__(self, stackSize: int):
        # 表示栈内元素数量
        self.arr = [[] for _ in range(3)]  # 3个栈
        self.stackSize = stackSize

    def push(self, stackNum: int, value: int) -> None:
        # stackNum 栈下标，表示第几个栈
        # value 压入的值
        if len(self.arr[stackNum]) < self.stackSize:
            self.arr[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if self.arr[stackNum]:
            return self.arr[stackNum].pop()
        else:
            return -1

    def peek(self, stackNum: int) -> int:  # 只返回栈顶元素，不出栈
        if self.arr[stackNum]:
            return self.arr[stackNum][-1]
        else:
            return -1

    def isEmpty(self, stackNum: int) -> bool:
        return len(self.arr[stackNum]) == 0
