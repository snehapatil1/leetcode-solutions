class Solution:
    def integerBreak(self, n: int) -> int:
        # dp = [0] * (n + 1)
        # dp[1] = 1

        # for i in range(2, n + 1):
        #     for j in range(1, i):
        #         dp[i] = max(dp[i], (max(j, dp[j]) * max(i - j, dp[i - j])))
        
        # return dp[-1]

        if n <= 3:
            return n - 1
        
        @cache
        def dp(num):
            if num <= 3:
                return num
            
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp(num - i))
            
            return ans
        
        return dp(n)
