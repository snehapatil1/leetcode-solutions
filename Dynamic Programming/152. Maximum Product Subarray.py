class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    n = len(nums)
    max_dp = [0] * n
    min_dp = [0] * n
    max_dp[0], min_dp[0] = nums[0], nums[0]
    for idx in range(1, n):
      max_dp[idx] = max(nums[idx], max_dp[idx - 1] * nums[idx], min_dp[idx - 1] * nums[idx])
      min_dp[idx] = min(nums[idx], max_dp[idx - 1] * nums[idx], min_dp[idx - 1] * nums[idx])
    
    return max(max_dp)
