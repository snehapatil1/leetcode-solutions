class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []

        def backtracking(openP, closeP):
            # if open and close parantheses == n
            if openP == closeP == n:
                output.append("".join(stack))
                return
            
            # if open parantheses < n
            if openP < n:
                stack.append("(")
                backtracking(openP + 1, closeP)
                stack.pop()
            
            # if close parantheses < open parantheses
            if closeP < openP:
                stack.append(")")
                backtracking(openP, closeP + 1)
                stack.pop()

        backtracking(0, 0)
        return output
            