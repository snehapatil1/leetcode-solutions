class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False
        
        maxJump = i = 0

        while i < len(nums) and i <= maxJump:
            maxJump = max(maxJump, nums[i] + i)
            i += 1
        
        return i == len(nums)
