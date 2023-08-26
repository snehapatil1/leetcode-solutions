class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_element:
            self.min_element = val

    def pop(self) -> None:
        val = self.stack[-1]
        self.stack.pop(-1)
        if val == self.min_element:
            if self.stack:
                self.min_element = min(self.stack)
            else:
                self.min_element = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_element


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()