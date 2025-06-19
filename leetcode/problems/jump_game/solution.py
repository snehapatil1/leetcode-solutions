class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) - 1

        for idx in range(len(nums) - 1, -1, -1):
            if (idx + nums[idx]) >= last_position:
                last_position = idx
        
        return last_position == 0