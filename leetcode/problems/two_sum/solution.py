class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for ele1 in range(len(nums)):
        #     for ele2 in range(2, len(nums)):
        #         if (nums[ele1-1] + nums[ele2-1]) == target:
        #             return [ele1-1, ele2-1]
        # return []
        ele1 = 0
        # ele2 = 1
        while ele1 < len(nums):
            ele2 = ele1 + 1
            while ele2 < len(nums):
                if (nums[ele1] + nums[ele2]) == target:
                    return [ele1, ele2]
                ele2 += 1
            ele1 += 1