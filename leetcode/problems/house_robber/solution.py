class Solution:
    def rob(self, nums: List[int]) -> int:
        one_back, two_back = 0, 0

        for num in nums:
            temp = one_back
            one_back = max(num + two_back, one_back)
            two_back = temp
        
        return one_back