class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        self.intervals.append([left, right])
        self.intervals.sort()
        merged = [self.intervals[0]]

        for start, end in self.intervals:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        self.intervals = merged

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.intervals:
            if start <= left and right <= end:
                return True
        
        return False

    def removeRange(self, left: int, right: int) -> None:
        temp = []
        
        for start, end in self.intervals:
            if start <= left and right <= end:
                s1, e1 = start, left
                s2, e2 = right, end
                if s1 < e1:
                    temp.append([s1, e1])
                if s2 < e2:
                    temp.append([s2, e2])
                continue
            elif left <= start < right:
                start = right
            elif left <= end < right:
                end = left
            
            if start < end:
                temp.append([start, end])

        self.intervals = temp

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)