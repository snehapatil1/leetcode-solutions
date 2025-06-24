class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        visited1 = set()
        visited2 = defaultdict(int)

        for idx1, num1 in enumerate(nums):
            if num1 not in visited1:
                visited1.add(num1)
                for idx2, num2 in enumerate(nums[idx1 + 1:]):
                    num3 = -num1 -num2
                    if num3 in visited2 and visited2[num3] == idx1:
                        output.add(tuple(sorted([num1, num2, num3])))
                    visited2[num2] = idx1
        
        return [list(op) for op in output]