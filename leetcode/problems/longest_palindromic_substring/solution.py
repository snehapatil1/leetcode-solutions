class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ''

        def helper_function(s, l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]
        
        # pick one letter and spread left and right to check if left == right
        for i in range(len(s)):
            output = max(helper_function(s, i, i), helper_function(s, i, i+1), output, key=len)
        
        return output