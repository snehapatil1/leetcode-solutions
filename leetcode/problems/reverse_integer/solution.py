class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            num = int(str(x)[::-1])
        else:
            num = - int(str(abs(x))[::-1])
        
        return num if abs(num) < ((2**31) - 1) else 0