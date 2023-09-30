class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        stack = []
        s3 = -float('inf')

        for num in nums[::-1]:
            if num < s3:
                return True
            while stack and stack[-1] < num:
                s3 = stack.pop()
            stack.append(num)
        return False