class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
        res = []
        dfs(nums, [], res)
        return res