class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(needle), len(haystack)
        if m < n:
            return -1
        for i in range(m):
            if haystack[i:i+n] == needle:
                return i
        
        return -1