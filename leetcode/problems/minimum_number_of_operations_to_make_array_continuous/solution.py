class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        output = n
        numsSet = sorted(set(nums))

        for i in range(len(numsSet)):
            left = numsSet[i]
            right = left + n - 1
            j = bisect_right(numsSet, right)
            count = j - i
            output = min(output, n - count)
        
        return output