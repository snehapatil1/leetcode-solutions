class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(remainingDice, target):
            if remainingDice == 0 and target == 0:
                return 1
            if remainingDice <= 0 or target <= 0:
                return 0
            
            return sum(dp(remainingDice - 1, target - i) for i in range(1, k + 1))

        
        return dp(n, target) % MOD
    