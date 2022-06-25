class Solution:
    def fib(self, n: int) -> int:
        def rec(x):
            if x == 0:
                return 0
            if x == 1:
                return 1

            return rec(x-1) + rec(x-2)
    
        ans = rec(n)
        
        return ans