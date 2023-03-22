class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        start, end = 0, len(list(s)) - 1
        while start < end:
            if s[start] != s[end]:
                return check_palindrome(s, start, end - 1) or check_palindrome(s, start + 1, end)
            start += 1
            end -= 1
        
        return True
