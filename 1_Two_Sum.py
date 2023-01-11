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
