class Solution:
    def countSubstrings(self, s: str) -> int:
        if not len(s):
            return 0
        
        self.count = 0
        def helper(s, l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                self.count += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            helper(s, i, i)
            helper(s, i, i + 1)
        
        return self.count