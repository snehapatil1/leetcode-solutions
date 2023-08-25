class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        
        if s3_len != (s1_len + s2_len): # if lengths don't match then s3 is an invalid string
            return False
        
        dp = [[False] * (s2_len + 1) for i in range(s1_len + 1)] # initialize dp with False for all cells
        dp[s1_len][s2_len] = True # last row col will be True since s3 is a valid string

        # let's traverse the string from end to start
        for i1 in range(s1_len, -1, -1):
            for i2 in range(s2_len, -1, -1):
                # if either s1 or s2 character == s3 position then move respective pointer of s1/s2 1 step forward and see if you reach end then set True
                if (i1 < s1_len and s1[i1] == s3[i1 + i2] and dp[i1 + 1][i2]) or (i2 < s2_len and s2[i2] == s3[i1 + i2] and dp[i1][i2 + 1]):
                    dp[i1][i2] = True
        return dp[0][0]