class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited_val1 = set()
        visited_val2 = defaultdict(int)
        output = set()

        for idx1, num1 in enumerate(nums):
            if num1 not in visited_val1:
                visited_val1.add(num1)
                for idx2, num2 in enumerate(nums[idx1+1:]):
                        num3 = -num1 - num2
                        if num3 in visited_val2 and num1 == visited_val2[num3]:
                            output.add(tuple(sorted([num1, num2, num3])))
                        visited_val2[num2] = num1
        return output