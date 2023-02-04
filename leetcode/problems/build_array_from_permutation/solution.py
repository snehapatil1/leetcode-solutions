class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        numsLen = len(nums)

        for idx in range(numsLen):
            ans.append(nums[nums[idx]])
        
        return ans