"""
    Question:
        Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
        There is only one repeated number in nums, return this repeated number.
        You must solve the problem without modifying the array nums and uses only constant extra space.
"""

from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return counts.most_common()[0][0]
