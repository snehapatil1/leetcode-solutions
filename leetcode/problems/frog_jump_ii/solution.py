class Solution:
    def maxJump(self, stones: List[int]) -> int:
        no_of_stones = len(stones)
        if no_of_stones == 2:
            return stones[1] - stones[0]
        
        max_jump = 0
        src, dest = 0, 2

        while dest < no_of_stones:
            max_jump = max(max_jump, stones[dest] - stones[src])
            src += 1
            dest += 1
        
        return max_jump
