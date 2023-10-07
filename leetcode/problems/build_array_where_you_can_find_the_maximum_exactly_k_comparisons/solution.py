class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(idx, maxSoFar, k):      
            if idx == n:
                if k == 0:
                    return 1
                return 0
            ans = 0
            for j in range(1, m + 1):
                ans += dp(idx + 1, max(maxSoFar, j), k - (j > maxSoFar))
            return ans % MOD
        
        return dp(0, -1, k)
            
        