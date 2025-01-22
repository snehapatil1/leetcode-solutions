class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in hmap:
                return [hmap[num2], i]
            hmap[nums[i]] = i