class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        dp = [0] * n
        output = 0

        def getLongestChain(i):
            if dp[i] != 0:
                return dp[i]
            
            dp[i] = 1
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], getLongestChain(j) + 1)
            
            return dp[i]
        
        for i in range(n):
            output = max(output, getLongestChain(i))
        
        return output