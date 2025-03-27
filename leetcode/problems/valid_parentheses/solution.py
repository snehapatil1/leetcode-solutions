class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        reverse_pair = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in pairs.keys():
                stack.append(i)
            else:
                if (not stack) or (stack[-1] != reverse_pair[i]):
                    return False
                stack.pop()
        return not stack