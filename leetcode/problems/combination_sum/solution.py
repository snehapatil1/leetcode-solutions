class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(i, curr, total):
            if total == 0:
                combinations.append(curr[:])
                return
            
            if total < 0:
                return
            
            for idx in range(i, len(candidates)):
                curr.append(candidates[idx])
                backtrack(idx, curr, total - candidates[idx])
                curr.pop()
        
        backtrack(0, [], target)

        return combinations