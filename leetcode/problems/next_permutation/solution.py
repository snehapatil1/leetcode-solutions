class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        breakPoint = -1

        for idx in range(n - 1, -1, -1):
            if nums[idx - 1] < nums[idx]:
                breakPoint = idx - 1
                break
        
        if breakPoint == -1:
            nums.reverse()
            return nums
        
        for idx in range(n - 1, breakPoint, -1):
            if nums[breakPoint] < nums[idx]:
                nums[breakPoint], nums[idx] = nums[idx], nums[breakPoint]
                break

        nums[breakPoint + 1:] = reversed(nums[breakPoint + 1:])
        
        return nums