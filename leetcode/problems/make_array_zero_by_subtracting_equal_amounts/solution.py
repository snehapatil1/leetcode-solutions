class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nset = set(nums)
        return len(nset) - (0 in nset)