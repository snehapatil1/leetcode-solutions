class Solution:
    def getSum(self, n:int):
        digits = [int(digit) for digit in str(n)]
        finalSum = 0
        for num in digits:
            finalSum += num ** 2

        return finalSum
    
    def isHappy(self, n: int) -> bool:
        used_nums = []
        while n != 1 and n not in used_nums:
            used_nums.append(n)
            n = self.getSum(n)
        
        return n == 1
