class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chmap = defaultdict(str)

        if len(s) != len(t):
            return False
        
        if len(set(s)) != len(set(t)):
            return False
        
        for idx in range(len(s)):
            if s[idx] not in chmap:
                chmap[s[idx]] = t[idx]
                continue
            if s[idx] in chmap and chmap[s[idx]] != t[idx]:
                return False
        
        return True