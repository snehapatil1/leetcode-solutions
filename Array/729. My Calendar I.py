class MyCalendar:
    def __init__(self):
        self.utilized = []

    def book(self, start: int, end: int) -> bool:
        for _start, _end in self.utilized:
            if _start < end and start < _end:
                return False
        self.utilized.append((start, end))
        self.utilized.sort()
        return True
    
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
