class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res, i = [], 0
        nums.sort()
        while i < len(nums):
            if nums[i+2] - nums[i] > k:
                return []
            res.append(nums[i:i+3])
            i += 3
        return res
        