class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # sort points
        points.sort()
        # make a set of unique points
        points_set = set(map(tuple, points))
        area = float('inf')

        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i:], i):
                # x1 should be less than x2 and y1 should be less than y2, and cross points should be in the set which means we have a diagonal
                if x1 < x2 and y1 < y2 and (x1, y2) in points_set and (x2, y1) in points_set:
                    cur_area = (x2 - x1) * (y2 - y1)
                    area = min(area, cur_area)
        
        return 0 if area == float('inf') else area