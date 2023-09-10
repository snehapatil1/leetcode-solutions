class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        if timestamp < self.timeMap[key][0][0]:
            return ""
        
        left, right = 0, len(self.timeMap[key])
        while left < right:
            mid = (left + right) // 2
            if timestamp >= self.timeMap[key][mid][0]:
                left = mid + 1
            else:
                right = mid
        return "" if right == 0 else self.timeMap[key][right - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)