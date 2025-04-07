class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        nums.sort()
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums: #11
            for i in range(target, num - 1, -1): #11 10
                dp[i] = dp[i] or dp[i - num]
        return dp[target]
