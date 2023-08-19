class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for num1 in range(len(nums) - 1):
            for num2 in range(num1 + 1, len(nums)):
                if nums[num1] + nums[num2] < target:
                    count += 1
        return count