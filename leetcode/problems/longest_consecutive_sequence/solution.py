class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                length = 1
                while (num + length) in nums:
                    length += 1
                maxlen = max(maxlen, length)

        return maxlen