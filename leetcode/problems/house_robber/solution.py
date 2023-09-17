class Solution:
    def rob(self, nums: List[int]) -> int:
        # ========== Bottom Up DP
        
        # n = len(nums)
        # if n <= 2:
        #     return max(nums)
        
        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # idx = 2

        # while idx < n:
        #     dp[idx] = max(dp[idx - 1], nums[idx] + dp[idx - 2])
        #     idx += 1
        
        # return max(dp)

        # ========== Bottom Up DP Space Optimized

        one_back, two_back = 0, 0

        for num in nums:
            temp = one_back
            one_back = max(num + two_back, one_back)
            two_back = temp
        
        return one_back