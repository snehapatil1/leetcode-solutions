class Solution:
    def myAtoi(self, s: str) -> int:
        numString = ""
        sign = 1
        ptr, n = 0, len(s)

        while ptr < n and s[ptr] == " ":
            ptr += 1
        
        if ptr < n and s[ptr] in ("-", "+"):
            sign = -1 if s[ptr] == "-" else 1
            ptr += 1
        
        while ptr < n and s[ptr].isdigit():
            numString += s[ptr]
            ptr += 1
        
        return max(-2**31, min(sign * int(numString or 0), 2**31 - 1))