class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for ch in s:
            if ch not in pairs:
                if not stack or ch != pairs[stack[-1]]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return stack == []