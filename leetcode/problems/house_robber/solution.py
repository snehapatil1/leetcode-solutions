class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        idx = 2

        while idx < n:
            dp[idx] = max(dp[idx - 1], nums[idx] + dp[idx - 2])
            idx += 1
        
        return max(dp)