class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        for idx in range(1, n):
            output[idx] = nums[idx - 1] * output[idx - 1]
        
        right_product = 1
        for idx in range(n - 1, -1, -1):
            output[idx] *= right_product
            right_product *= nums[idx]
        
        return output