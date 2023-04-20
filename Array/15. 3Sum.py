"""
    Question:
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums_len = len(nums)
        # final output array
        output = set()
        
        # visited num2
        visited_val2 = {}
        
        # visited num1
        visited_val1 = set()
        
        # if given array len < 3 then it is not a valid array hence return
        if nums_len < 3:
            return []
        
        # if given array len is 3 and it sums to 0 then return that array
        if nums_len == 3 and sum(nums) == 0:
            output.add(tuple(nums))
            return output
        
        for idx1, val1 in enumerate(nums):
            # if val1 is not visited earlier then only proceed
            if val1 not in visited_val1:
                # add val1 in visited
                visited_val1.add(val1)
                
                for idx2, val2 in enumerate(nums[idx1+1:]):
                    # derive val3 as (0 - (val1 + val2))
                    val3 = -val1 -val2
                
                    # if val3 is present in visited val 2 keys and valye of key val3 is same as val1 then append it in output
                    if (val3 in visited_val2 and visited_val2[val3] == val1):
                        output.add(tuple(sorted((val1, val2, val3))))
                    
                    # set val1 value in val2 in visited val2 dict
                    visited_val2[val2] = val1
        
        return output
