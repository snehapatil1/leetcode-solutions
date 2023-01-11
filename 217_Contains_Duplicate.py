"""
    Data Structures: Array, Set
    Time Complexity: O(1)
    Space Complexity: O(1)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original_length = len(nums)
        unique_nums_length = len(set(nums))
        if unique_nums_length < original_length:
            return True
        return False
