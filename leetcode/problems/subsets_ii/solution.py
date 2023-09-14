class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        nums.sort()

        def backtracking(first, curr, k):
            if len(curr) == k:
                if curr not in combinations:
                    combinations.append(curr[:])
                return
            for i in range(first, len(nums)):
                curr.append(nums[i])
                backtracking(i + 1, curr, k)
                curr.pop()
        
        for k in range(len(nums) + 1):
            backtracking(0, [], k)
        
        return combinations