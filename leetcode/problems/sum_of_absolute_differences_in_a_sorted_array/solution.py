class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        left_sum = 0
        total_sum = sum(nums)

        for idx in range(n):
            right_sum = total_sum - left_sum - nums[idx]
            left_count = idx
            right_count = n - 1 - idx
            left_total = nums[idx] * left_count - left_sum
            right_total = right_sum - nums[idx] * right_count

            result.append(left_total + right_total)
            left_sum += nums[idx]
        
        return result
