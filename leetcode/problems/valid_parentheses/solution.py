class Solution:
    def isValid(self, s: str) -> bool:
        is_satisfied = self.areConstraintsSatisfied(s)
        if (not is_satisfied):
            return False
        
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        
        stack = []
        for ele in s:
            if ele in pairs.keys():
                stack.append(ele)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if ele != pairs[a]:
                    return False
        return stack == []
    
    def areConstraintsSatisfied(self, s):
        if (len(s) < 1) or (len(s) > 10**4):
            return False
        for ele in s:
            if ele not in ('(', ')', '{', '}', '[', ']'):
                return False
        if len(s) % 2 != 0:
            return False
        return True