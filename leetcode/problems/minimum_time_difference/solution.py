import time
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        s = sorted([int((int(i[:2])*60)+int(i[3:])) for i in timePoints])
        s.append(s[0]+1440)
        minimum = s[-1] - s[0]
        
        for i in range(len(s)-1):
            minimum = min(minimum, s[i+1]-s[i])
            if (not minimum):
                return minimum
        return minimum