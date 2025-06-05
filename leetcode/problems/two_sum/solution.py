class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for idx, num in enumerate(nums):
            if num in hmap:
                return [hmap[num], idx]
            new_num = target - num
            hmap[new_num] = idx
