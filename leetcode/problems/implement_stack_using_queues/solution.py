class MyStack:

    # def __init__(self):
    #     self.stack = collections.deque()
    #     self.current_top = float('inf')

    # def push(self, x: int) -> None:
    #     self.stack.append(x)
    #     self.current_top = x

    # def pop(self) -> int:
    #     popped = self.stack.pop()
    #     if self.stack:
    #         self.current_top = self.stack[-1]
    #     else:
    #         self.current_top = float('inf')
    #     return popped

    # def top(self) -> int:
    #     return self.current_top if self.current_top != float('inf') else -1

    # def empty(self) -> bool:
    #     return len(self.stack) == 0

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()