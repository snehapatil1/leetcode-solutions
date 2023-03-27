class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        
        for i in range(1, n + 1):
            num = set(list(str(i)))
            if (not num.intersection({'3', '4', '7'})) and num.intersection({'2', '5', '6', '9'}):
                count += 1
            
        return count