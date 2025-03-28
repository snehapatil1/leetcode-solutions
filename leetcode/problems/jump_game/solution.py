class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_position = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        return last_position == 0