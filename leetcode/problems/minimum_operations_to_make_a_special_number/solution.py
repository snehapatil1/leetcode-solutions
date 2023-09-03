class Solution:
    def minimumOperations(self, num: str) -> int:
        operations = float('inf')
        n = len(num)
        valid = [0, 25, 50, 75]
        
        for i in range(n):
            for j in range(i + 1, n):
                if int(num[i])*10 + int(num[j]) in valid:
                    operations = min(operations, n - 2 - i)
        
        if operations == float('inf'):
            if '0' in num:
                return n - 1
            else:
                return n
        
        return operations