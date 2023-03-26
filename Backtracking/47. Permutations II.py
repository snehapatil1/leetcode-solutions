class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(nums, curr):
            if not nums:
                if curr[:] not in permutations:
                    permutations.append(curr[:])
            
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], curr+[nums[i]])
        
        backtrack(nums, [])

        return permutations
