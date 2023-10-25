class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        output, arrow = 0, 0

        for start, end in points:
            if output == 0 or start > arrow:
                output += 1
                arrow = end
        
        return output