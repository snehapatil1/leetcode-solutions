class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ''
        word1_start = 0
        word2_start = 0
        word1_len = len(word1)
        word2_len = len(word2)

        while (word1_start < word1_len) or (word2_start < word2_len):
            if word1_start < word1_len:
                new_string += word1[word1_start]
                word1_start += 1
            
            if word2_start < word2_len:
                new_string += word2[word2_start]
                word2_start += 1
        
        return new_string
