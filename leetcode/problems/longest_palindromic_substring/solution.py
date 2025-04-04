class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return end - start - 1
                
        output = [0, 0]
        for i in range(len(s)):
            odd_length = helper(i, i)
            if odd_length > output[1] - output[0] + 1:
                dist = odd_length // 2
                output = [i - dist, i + dist]
            even_length = helper(i, i + 1)
            if even_length > output[1] - output[0] + 1:
                dist = (even_length // 2) - 1
                output = [i - dist, i + dist + 1]
        
        return s[output[0]:output[1] + 1]