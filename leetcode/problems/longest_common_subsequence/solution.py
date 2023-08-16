class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        text1 = " " + text1
        text2 = " " + text2

        for t1 in range(1, len(text1)):
            for t2 in range(1, len(text2)):
                if text1[t1] == text2[t2]:
                    dp[t1][t2] = 1 + dp[t1 - 1][t2 - 1]
                else:
                    dp[t1][t2] = max(dp[t1 - 1][t2], dp[t1][t2 - 1])
        
        return dp[-1][-1]