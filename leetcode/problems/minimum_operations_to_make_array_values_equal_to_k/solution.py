class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        ops = 0
        for num in nums_set:
            if num < k:
                return -1
            elif num > k:
                ops += 1
        return ops