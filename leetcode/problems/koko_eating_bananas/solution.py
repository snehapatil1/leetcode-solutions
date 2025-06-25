class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n == h:
            return max(piles)
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            time = 0
            for num in piles:
                time += ceil(num / mid)
            if time <= h:
                right = mid
            else:
                left = mid + 1
        
        return right