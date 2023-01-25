class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        
        for i in range(zero_count):
            nums.append(0)