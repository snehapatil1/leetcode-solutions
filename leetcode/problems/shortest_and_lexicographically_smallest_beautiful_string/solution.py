class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        
        if n == k and s.count("1") == k:
            return s
        
        p1, p2 = 0, 0
        shortestString = ""
        
        while p1 <= p2 < n:
            oneCounter = s[p1: p2 + 1].count("1")
            if oneCounter == k:
                if shortestString == "" or (p2 - p1 + 1) < len(shortestString) or ((p2 - p1 + 1) == len(shortestString) and s[p1: p2 + 1] < shortestString):
                    shortestString = s[p1: p2 + 1]
                    p1 += 1
                    p2 = p1
                    continue
            
            p2 += 1
            if p2 == n:
                p1 += 1
                p2 = p1
        return shortestString