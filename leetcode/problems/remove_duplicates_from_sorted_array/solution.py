class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        update_index = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                nums[update_index] = nums[i]
                update_index += 1
        return update_index