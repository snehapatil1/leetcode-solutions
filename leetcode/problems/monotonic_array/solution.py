class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp = [num for num in nums]
        if nums[0] <= nums[-1]:
            nums.sort()
        else:
            nums.sort(reverse=True)
        return temp == nums
        