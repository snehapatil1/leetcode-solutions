class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(mins, sec):
            if mins < 0 or mins > 99 or sec < 0 or sec > 99:
                return float('inf')
            
            s = str((mins * 100) + sec)
            curr = str(startAt)
            val = 0

            for ch in s:
                if ch == curr:
                    val += pushCost
                else:
                    val += (moveCost + pushCost)
                    curr = ch
            return val
        
        mins, sec = targetSeconds // 60, targetSeconds % 60
        return min(cost(mins, sec), cost(mins - 1, sec + 60))