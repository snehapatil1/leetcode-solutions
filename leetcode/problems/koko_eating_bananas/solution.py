class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        start, end = 1, max(piles)
        
        while start < end:
            mid = (start + end) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            
            if time <= h:
                end = mid
            else:
                start = mid + 1
        
        return end
