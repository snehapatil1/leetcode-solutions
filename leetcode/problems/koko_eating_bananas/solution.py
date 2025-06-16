from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        if n == h:
            return max(piles)
        
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            count = 0
            for p in piles:
                count += ceil(p / mid)
            if count <= h:
                r = mid
            else:
                l = mid + 1
        
        return r