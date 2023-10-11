
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1

        while p1 <= p2:
            if (s[p1].isalpha() or s[p1].isdigit()) and (s[p2].isalpha() or s[p2].isdigit()):
                if s[p1].lower() != s[p2].lower():
                    return False
                p1 += 1
                p2 -= 1
            elif not s[p1].isalpha() and not s[p1].isdigit():
                p1 += 1
            elif not s[p2].isalpha() and not  s[p2].isdigit():
                p2 -= 1
        
        return True