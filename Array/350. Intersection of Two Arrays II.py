"""
    Question:
        Given two integer arrays nums1 and nums2, return an array of their intersection. 
        Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

"""
    Data Structures: Collections, Hash Map
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = collections.Counter(nums1)
        res = []

        for num in nums2:
            if n1[num] > 0:
                res.append(num)
                n1[num] -= 1
        
        return res
