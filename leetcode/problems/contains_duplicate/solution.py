class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) < len(nums):
            return True
        else:
            return False
        # for element in nums:
        #     if nums.count(element) >= 2:
        #         return True
        # return False

obj = Solution()
obj.containsDuplicate([1,2,3,1])
obj.containsDuplicate([1,2,3,4])
obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
