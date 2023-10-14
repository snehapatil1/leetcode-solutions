class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        # n = 4, words = ["a","b","c","d"], groups = [1,0,1,1]
        output = []
        if n == 1:
            return words
        
        p1, p2 = 0, 1
        while p1 < p2 < n:
            if groups[p1] != groups[p2]:
                if words[p1] not in output:
                    output.append(words[p1])
                if words[p2] not in output:
                    output.append(words[p2])
                p1 = p2
            p2 += 1
        
        if not output:
            output.append(words[0])
        return output