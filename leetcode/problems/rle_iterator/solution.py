class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding

    def next(self, n: int) -> int:
        num = -1
        while self.encoding and n > 0:
            if n <= self.encoding[0]:
                self.encoding[0] -= n
                n = 0
                num = self.encoding[1]
            else:
                n -= self.encoding[0]
                self.encoding[0] = 0
            
            if self.encoding[0] == 0:
                self.encoding.pop(0)
                self.encoding.pop(0)

        if n > 0:
            return -1
        
        return num

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)