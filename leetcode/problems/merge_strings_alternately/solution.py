class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        w1, w2 = len(word1), len(word2)
        ptr = 0

        while ptr < w1 or ptr < w2:
            if ptr < w1:
                output += word1[ptr]
            if ptr < w2:
                output += word2[ptr]
            ptr += 1

        return output