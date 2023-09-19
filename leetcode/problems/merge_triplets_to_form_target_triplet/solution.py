class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        op = [0] * 3
        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                op = [max(x, op[0]), max(y, op[1]), max(z, op[2])]
        return op == target
                