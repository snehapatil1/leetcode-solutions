class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxRobbery(nums):
            one_back, two_back = 0, 0

            for num in nums:
                temp = max(num + one_back, two_back)
                one_back = two_back
                two_back = temp
            
            return two_back
        
        return max(nums[0], maxRobbery(nums[1:]), maxRobbery(nums[:-1]))
