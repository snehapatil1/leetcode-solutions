class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n

        left, right, curr = 0, n - 1, n - 1

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                num = nums[right]
                right -= 1
            else:
                num = nums[left]
                left += 1
            output[curr] = num * num
            curr -= 1
        
        return output