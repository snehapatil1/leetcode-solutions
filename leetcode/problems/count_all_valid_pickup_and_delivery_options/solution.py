class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 1

        for i in range(1, 2 * n + 1):
            ans = ans * i
            if not i % 2:
                ans = ans // 2
            ans %= MOD
        
        return ans