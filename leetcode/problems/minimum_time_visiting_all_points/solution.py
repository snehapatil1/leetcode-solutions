class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        output = 0

        for idx in range(len(points) - 1):
            x, y = points[idx]
            tx, ty = points[idx + 1]
            output += max(abs(tx - x), abs(ty - y))

        return output