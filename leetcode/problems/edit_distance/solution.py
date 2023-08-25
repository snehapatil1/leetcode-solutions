class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for row in range(m + 1):
            dp[row][0] = row
        
        for col in range(n + 1):
            dp[0][col] = col
        
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
        return dp[-1][-1]