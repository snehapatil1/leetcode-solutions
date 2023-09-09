class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s) != len(words):
            return False
        for idx in range(len(words)):
            if words[idx][0] != s[idx]:
                return False
        return True