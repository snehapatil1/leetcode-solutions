"""
    Question:
        Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than ⌊n / 2⌋ times. 
        You may assume that the majority element always exists in the array.
"""

import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_times = math.ceil(len(nums) / 2)
        nums_set = set(nums)
        for num in nums_set:
            if nums.count(num) >= majority_times:
                return num
