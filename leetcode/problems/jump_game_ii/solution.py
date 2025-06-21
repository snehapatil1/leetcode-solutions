class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest_jump = 0
        end = 0
        for start in range(len(nums) - 1):
            farthest_jump = max(farthest_jump, start + nums[start])
            if start == end:
                jumps += 1
                end = farthest_jump

        return jumps