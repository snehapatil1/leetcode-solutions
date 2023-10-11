class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for ch in path.split('/'):
            if stack and ch == '..':
                stack.pop()
            elif ch not in ['.', '..', '']:
                stack.append(ch)
        
        return "/" + "/".join(stack)