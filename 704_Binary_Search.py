class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        start = 0
        end = nums_len - 1

        if nums_len == 1 and target in nums:
            return 0

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
            
        return -1
