class Solution:
    def jump(self, nums: List[int]) -> int:
        start, nextJump = 0, 0
        maxJump, minJumps = 0, 0
        while nextJump < (len(nums) - 1):
            for i in range(start, nextJump + 1):
                maxJump = max(maxJump, nums[i] + i)
            start = nextJump + 1
            nextJump = maxJump
            minJumps += 1
        return minJumps