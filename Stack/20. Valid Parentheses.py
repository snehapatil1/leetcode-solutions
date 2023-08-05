"""
    Question:
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        stack = []

        s_arr = list(s)

        for ele in range(len(s_arr)):
            val = s_arr[ele]

            if val in pairs.keys():
                stack.append(val)
            else:
                if stack and stack[len(stack)-1] == [a for a in pairs if pairs[a] == val][0]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        
        return False
