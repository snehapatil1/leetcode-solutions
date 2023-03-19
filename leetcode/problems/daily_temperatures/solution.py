class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        op = [0] * n
        stack = []

        for i, j in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < j:
                n = stack.pop()
                op[n] = i - n
            stack.append(i)
        
        return op