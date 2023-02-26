class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ele in tokens:
            if (ele.isalpha()) and (ele not in ["+", "-", "*", "/"]):
                return 0
            
            if ele in ["+", "-", "*", "/"]:
                val1 = stack.pop()
                val2 = stack.pop()
            
                if ele == "+":
                    res = val1 + val2
                if ele == "-":
                    res = val2 - val1
                if ele == "*":
                    res = val1 * val2
                if ele == "/":
                    res = val2 / val1
                
                stack.append(int(res))
            else:
                stack.append(int(ele))
            
        output = stack.pop()
        return output