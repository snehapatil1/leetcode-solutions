class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = self.get_product(nums)
        
        if product < 0:
            return -1
        elif product > 0:
            return 1
        else:
            return 0
    
    def get_product(self, nums):
        product = 1

        for num in nums:
            product *= num
        
        return product