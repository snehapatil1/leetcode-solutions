import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_times = math.ceil(len(nums) / 2)
        nums_set = set(nums)
        for num in nums_set:
            if nums.count(num) >= majority_times:
                return num
