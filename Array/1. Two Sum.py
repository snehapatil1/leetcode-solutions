"""
    Question:
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
"""

"""
    Data Structures: Array, Hash Table
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for idx, ele in enumerate(nums):
            if (target - ele) in index_dict:
                return [idx, index_dict[target - ele]]
            index_dict[ele] = idx
