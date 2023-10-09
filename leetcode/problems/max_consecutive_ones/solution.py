class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0

        counter = 0
        for idx, num in enumerate(nums):
            if num == 1:
                counter += 1
            else:
                counter = 0
            maxLen = max(maxLen, counter)

        return maxLen