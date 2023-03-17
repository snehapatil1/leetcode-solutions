class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def backtrack(first, curr):
            if len(curr) == k:
                output.append(curr[:])
            
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(1, [])

        return output