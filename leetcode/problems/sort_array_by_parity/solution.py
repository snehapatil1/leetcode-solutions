class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # evenArray, oddArray = [], []

        # for num in nums:
        #     if num % 2:
        #         oddArray.append(num)
        #     else:
        #         evenArray.append(num)
        
        # evenArray.extend(oddArray)
        # return evenArray

        def swap(nums, start, end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] % 2 == 0:
                start += 1
            else:
                if nums[end] % 2:
                    end -= 1
                else:
                    swap(nums, start, end)
                    start += 1
                    end -= 1

        return nums
