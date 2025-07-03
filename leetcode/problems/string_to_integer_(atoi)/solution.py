class Solution:
    def myAtoi(self, s: str) -> int:
        num_string = ""
        p, n = 0, len(s)
        sign = 1

        while p < n and s[p] == " ":
            p += 1
        
        if p < n and s[p] in ["+", "-"]:
            sign = -1 if s[p] == "-" else 1
            p += 1
        
        while p < n and s[p].isdigit():
            num_string += s[p]
            p += 1
        
        return max(-2**31, min(sign * int(num_string or 0), 2**31 - 1))