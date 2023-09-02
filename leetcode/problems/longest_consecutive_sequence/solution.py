class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        output = 0
        numsSet = set(nums)
        for n in nums:
            if (n - 1) not in numsSet:
                length = 1
                while n + length in numsSet:
                    length += 1
                output = max(output, length)
        return output