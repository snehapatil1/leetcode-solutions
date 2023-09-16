class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        # n = len(nums)
        # minNum = min(nums)
        # minIndex = nums.index(minNum)
        # if minIndex == 0:
        #     temp = [num for num in nums]
        #     temp.sort()
        #     if temp == nums:
        #         return 0
        # rightShifts = n - minIndex
        # newNums = [-1] * n
        # for idx in range(n):
        #     newIndex = idx + rightShifts
        #     if newIndex >= n:
        #         newIndex = newIndex - n
        #     newNums[newIndex] = nums[idx]
        
        # nums.sort()
        # if newNums == nums:
        #     return rightShifts
        # return -1

        n, total, res = len(nums), 0, sorted(nums)

        while total <= n:
            nums = [nums[-1]] + nums[:-1]
            total += 1

            if nums == res:
                return total%n

        return -1




