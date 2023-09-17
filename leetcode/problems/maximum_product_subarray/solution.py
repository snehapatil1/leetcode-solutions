class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    curMax, curMin = 1, 1
    product = nums[0]

    for num in nums:
        temp = curMax * num
        curMax = max(curMax * num, curMin * num, num)
        curMin = min(temp, curMin * num, num)
        product = max(product, curMax)
    
    return product