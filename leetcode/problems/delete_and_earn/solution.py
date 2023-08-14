class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # for each number in nums use that as idx and at that idx store sum of number of those numbers
        scores = [0] * (max(nums) + 1)
        for num in nums:
            scores[num] += num
        
        dp = [0] * (len(scores))
        dp[0] = scores[0]
        dp[1] = max(scores[0], scores[1])

        # current idx score + dp - 2 -> current idx score because if we choose to delete this num and dp - 2 because since we choose to delete current num, dp-1 will also get deleted so dp - 2 is available
        for i in range(2, len(scores)):
            dp[i] = max(scores[i] + dp[i - 2], dp[i - 1])
        
        return dp[-1]