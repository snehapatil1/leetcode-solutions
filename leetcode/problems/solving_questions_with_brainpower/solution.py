class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        res = [0] * n
        res[-1] = questions[-1][0]
        for i in range(n - 2, -1, -1):
            res[i] = questions[i][0]
            skip = questions[i][1]
            if i + skip + 1 < n:
                res[i] += res[i + skip + 1]
            res[i] = max(res[i], res[i + 1])
        return res[0]