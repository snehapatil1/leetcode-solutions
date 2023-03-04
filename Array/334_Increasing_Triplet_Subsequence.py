class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_number = float(inf)
        second_number = float(inf)
        
        for num in nums:
            if num <= first_number:
                first_number = num
            elif num <= second_number:
                second_number = num
            else:
                return True
        
        return False
