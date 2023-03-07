class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = len(nums) - 1
        curr = 0
        
        while curr <= p2:
            if nums[curr] == 0:
                nums[p1], nums[curr] = nums[curr], nums[p1]
                p1 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
