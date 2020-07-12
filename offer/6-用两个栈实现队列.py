class CQueue:

    def __init__(self):
        self.stack = []

    def appendTail(self, value: int) -> None:
        self.stack.append(value)

    def deleteHead(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop(0)


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(3)
print(obj.deleteHead())
print(obj.deleteHead())
