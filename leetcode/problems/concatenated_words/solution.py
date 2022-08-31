class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        res = set()
        def helper(s):
            if not s: return True
            
            check = ''
            for i in range(len(s)):
                check += s[i]
                if check in wordSet:
                    if helper(s[i + 1:]):
                        return True
            return False
        
        for word in wordSet:
            wordSet.remove(word)
            if helper(word):
                res.add(word)
            wordSet.add(word)
        return res