class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if (mid % 2 == 0 and nums[mid] == nums[mid - 1]) or (mid % 2 != 0 and nums[mid] == nums[mid + 1]):
                right = mid - 1
            else:
                left = mid + 1
            
        return nums[left - 1]