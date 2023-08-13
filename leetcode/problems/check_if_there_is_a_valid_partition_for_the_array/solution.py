class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # nums = [4,4,4,5,6]
        # dp =   [True, False, True, True, False, False]
        n = len(nums)
        # each index in dp represents is subarray till that index from start is valid or not
        dp = [False for _ in range(n + 1)]
        dp[0] = True

        for idx in range(1, n):
            # if atleast 1 of these 3 conditions are True then current sp index is True
            
            # Condition 1: current num and index-1 num are same and dp index - 1 is True
            if idx > 0 and nums[idx] == nums[idx - 1] and dp[idx - 1]:
                dp[idx + 1] = True
            
            # Condition 2: current num, index-1 num and index-2 num are same and dp index-2 is True
            if idx > 1 and nums[idx] == nums[idx - 1] == nums[idx - 2] and dp[idx - 2]:
                dp[idx + 1] = True
            
            # Condition 3: current num = index-1 num+1 and index-2 num+2 and dp index-2 is True
            if idx > 1 and nums[idx] == nums[idx - 1] + 1 == nums[idx - 2] + 2 and dp[idx - 2]:
                dp[idx + 1] = True

        return dp[-1]