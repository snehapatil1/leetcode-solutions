class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for idx1, num1 in enumerate(nums):
            if idx1 > 0 and num1 == nums[idx1 - 1]:
                continue
            
            left = idx1 + 1
            right = len(nums) - 1

            while left < right:
                target = num1 + nums[left] + nums[right]
                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                else:
                    output.append([num1, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return output