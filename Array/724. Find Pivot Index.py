class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_map = {}

        for idx in range(len(nums)):
            left_sum = sum(nums[:idx])
            right_sum = sum(nums[idx + 1:])
            if nums[idx] not in sum_map.keys():
                sum_map[nums[idx]] = 0
            sum_map[nums[idx]] = left_sum

            if left_sum == right_sum:
                return idx
        
        return -1
