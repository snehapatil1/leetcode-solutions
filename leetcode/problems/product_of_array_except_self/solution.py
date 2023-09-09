class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        leftProduct = [1] * n

        for idx in range(1, n):
            output[idx] = output[idx - 1] * nums[idx - 1]
        
        rightProduct = 1
        for idx in range(n - 1, -1, -1):
            output[idx] *= rightProduct
            rightProduct *= nums[idx]
        
        return output