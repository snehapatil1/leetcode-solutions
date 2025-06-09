class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for ch in s:
            if stack:
                if ch in pairs:
                    if pairs[ch] != stack[-1]:
                        return False
                    stack.pop()
                    continue
            stack.append(ch)
        
        return stack == []