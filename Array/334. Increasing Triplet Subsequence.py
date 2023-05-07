"""
    Question:
        Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
        such that i < j < k and nums[i] < nums[j] < nums[k].
        If no such indices exists, return false.
"""

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
