class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        operations, left, curSum = 0, 0, 0

        if target == 0:
            return n

        for right in range(n):
            curSum += nums[right]
            while left <= right and curSum > target:
                curSum -= nums[left]
                left += 1
            if curSum == target:
                operations = max(operations, right - left + 1)
        
        return n - operations if operations else -1