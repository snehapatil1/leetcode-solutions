class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        count = 1

        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                predecessor = word[0:i] + word[i + 1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
                    count = max(count, dp[word])
        
        return count