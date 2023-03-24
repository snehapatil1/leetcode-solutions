class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []

        def backtrack(index, k, total, curr):
            if k == 0 and total == 0:
                comb = curr[:]
                comb.sort()
                if comb not in combinations:
                    combinations.append(comb[:])
                    return True
            
            if k < 0 or total < 0:
                return True
            
            for i in range(index, 10):
                backtrack(i + 1, k - 1, total - i, curr+[i])
        
        backtrack(1, k, n, [])

        return combinations