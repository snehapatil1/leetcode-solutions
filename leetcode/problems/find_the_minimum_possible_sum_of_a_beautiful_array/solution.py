class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        if n == 1: return n
        
        nums = set()
        num = 1
        
        while n:
            if (target - num) not in nums:
                nums.add(num)
                n -= 1
            num += 1
        
        return sum(nums)