class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, cur=[]):
            if len(cur) == k:
                combinations.append(cur[:])
                return
            
            for i in range(first, n):
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()
        
        combinations = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        
        return combinations

