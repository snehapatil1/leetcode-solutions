class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i, j = len(word1), len(word2)
        n = max(len(word1), len(word2))
        for x in range(n):
            if x < i:
                merged += word1[x]
            if x < j:
                merged += word2[x]
        return merged
