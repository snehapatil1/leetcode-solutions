class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        def backtrack(first, curr, total):
            if total == 0:
                combinations.append(curr[:])
                return
            if total < 0:
                return
            
            for i in range(first, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, total - candidates[i])
                curr.pop()
        
        backtrack(0, [], target)
        return combinations