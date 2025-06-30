class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point = -1
        n = len(nums)
        for idx in range(n - 1, -1, -1):
            if nums[idx - 1] < nums[idx]:
                point = idx - 1
                break
        
        if point == -1:
            nums.reverse()
            return
        
        for idx in range(n - 1, point, -1):
            if nums[point] < nums[idx]:
                nums[point], nums[idx] = nums[idx], nums[point]
                break
        
        nums[point + 1:] = reversed(nums[point + 1:])