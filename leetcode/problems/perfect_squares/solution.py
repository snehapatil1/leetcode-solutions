class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        i = 1
        while i < n + 1:
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
            i += 1
        
        return dp[-1]