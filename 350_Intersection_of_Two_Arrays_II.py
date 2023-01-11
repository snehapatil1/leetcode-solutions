"""
    Data Structures: Collections
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
