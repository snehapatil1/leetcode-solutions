class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = ""
        for ch in s:
            if ch.isalnum():
                snew += ch.lower()
        return snew == snew[::-1]