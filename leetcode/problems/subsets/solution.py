class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)

        def backtrack(first=0, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
                return
            
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        for k in range(n + 1):
            backtrack()

        return output