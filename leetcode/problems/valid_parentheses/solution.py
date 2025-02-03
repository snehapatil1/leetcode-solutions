class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'}': '{', ')': '(', ']': '['}
        for ch in s:
            if ch in ['[', '{', '(']:
                stack.append(ch)
            else:
                if stack and pair[ch] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(ch)
        return stack == []