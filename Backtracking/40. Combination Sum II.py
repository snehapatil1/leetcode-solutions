class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(first, curr, total):
            if total == 0:
                if curr[:] not in combinations:
                    combinations.append(curr[:])
                return True
            
            if total < 0:
                return True
            
            for i in range(first, len(candidates)):
                if (i > first and candidates[i] == candidates[i - 1]):
                    continue
                curr.append(candidates[i])
                is_break = backtrack(i + 1, curr, total - candidates[i])
                curr.pop()
                if is_break:
                    break
        
        candidates.sort()
        backtrack(0, [], target)

        return combinations
