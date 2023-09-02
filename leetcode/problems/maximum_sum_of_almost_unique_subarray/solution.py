class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        maxSum = 0
        
        for start in range(len(nums) - k + 1):
            if len(set(nums[start: start + k])) >= m:
                maxSum = max(maxSum, sum(nums[start: start + k]))
        return maxSum