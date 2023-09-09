class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        output = 0
        nums = set()
        nums.add(1)
        i = 0
        
        while len(nums) < n:
            i += 1
            if k - i not in nums:
                nums.add(i)
        return sum(nums)