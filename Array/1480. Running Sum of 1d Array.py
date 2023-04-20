"""
    Question:
        Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
        Return the running sum of nums.
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        running_sum = 0
        for num in nums:
            running_sum += num
            output.append(running_sum)
        return output
