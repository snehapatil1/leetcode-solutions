import math
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prefix_zeros = -1
        max_zeros = -1
        sufix_zeros = -1
        zeros = 0
        
        for seat in seats:
            if seat == 0:
                zeros += 1
            else:
                if prefix_zeros == -1:
                    prefix_zeros = zeros
                else:
                    max_zeros = max(max_zeros, zeros)
                zeros = 0
        sufix_zeros = zeros
        
        return max(prefix_zeros, sufix_zeros, (max_zeros + 1)// 2)