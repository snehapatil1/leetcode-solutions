class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) < 2:
            if sum(nums) >= target:
                return len(nums)
            return 0
        
        total, minLen = 0, float('inf')
        p1, p2, n = 0, 0, len(nums)

        for p2 in range(n):
            total += nums[p2]
            
            while total >= target:
                minLen = min(minLen, p2 - p1 + 1)
                total -= nums[p1]
                p1 += 1
        
        return minLen if minLen != float('inf') else 0