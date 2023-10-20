class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = "".join(reversed(s))

        m, n = len(s) + 1, len(t) + 1
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        s = " " + s
        t = " " + t

        for i in range(1, m):
            for j in range(1, n):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m - 1][n - 1]