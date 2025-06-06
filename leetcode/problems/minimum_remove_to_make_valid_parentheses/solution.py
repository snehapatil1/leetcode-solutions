class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            elif ch == ')':
                if stack:
                    if s[stack[-1]] == '(':
                        stack.pop(-1)
                    else:
                        stack.append(idx)
                else:
                    stack.append(idx)

        while stack:
            idx = stack.pop()
            s = s[:idx] + s[idx + 1:]
        return s
