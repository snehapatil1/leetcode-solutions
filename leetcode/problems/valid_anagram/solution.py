class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = defaultdict(int), defaultdict(int)

        for idx in range(len(s)):
            countS[s[idx]] = countS.get(s[idx], 0) + 1
            countT[t[idx]] = countT.get(t[idx], 0) + 1
        
        return countS == countT