class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        operations, up = 0, 0
        nums.sort()
        n = len(nums)

        for idx in range(1, n):
            if nums[idx] != nums[idx - 1]:
                up += 1
            operations += up
        
        return operations