"""
    Question:
        Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
        You may return the answer in any order.
"""

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
