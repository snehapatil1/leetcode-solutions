class Solution:
    def calculate(self, s: str) -> int:
        ans, num, sign = 0, 0, 1
        stack = [sign]

        for ch in s:
            if ch == " ":
                continue
            
            if ch == "(":
                stack.append(sign)
            elif ch == ")":
                stack.pop()
            elif ch in ["+", "-"]:
                ans += num * sign
                sign = (1 if ch == "+" else -1) * stack[-1]
                num = 0
            elif ch.isdigit():
                num = num * 10 + (ord(ch) - ord('0'))
        
        return ans + sign * num