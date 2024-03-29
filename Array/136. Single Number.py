"""
    Question:
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            if i not in hash_map.keys():
                hash_map.update({i: 1})
            else:
                hash_map[i] += 1
        
        for i in hash_map:
            if hash_map[i] == 1:
                return i
