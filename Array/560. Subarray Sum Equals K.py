"""
    Question:
        Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
        A subarray is a contiguous non-empty sequence of elements within an array.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total_sum = 0
        hash_map = {0 : 1}
        
        for idx in range(len(nums)):
            total_sum += nums[idx]
            if (total_sum - k) in hash_map.keys():
                count += hash_map[total_sum - k]
            if total_sum in hash_map.keys():
                hash_map[total_sum] += 1
            else:
                hash_map.update({total_sum : 1})

        return count
