class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        output = 0

        sorted_startWords = set(["".join(sorted(word)) for word in startWords])
        sorted_targetWords = ["".join(sorted(word)) for word in targetWords]

        for word in sorted_targetWords:
            for i in range(len(word)):
                if word[:i] + word[i+1:] in sorted_startWords:
                    output += 1
                    break
        
        return output