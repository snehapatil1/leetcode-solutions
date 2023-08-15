class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(point1, point2):
            # square of (X points) + square of (Y points)
            return (((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))
        
        # get distance of each point from every other point and make it as a list and then sort that list
        D = [
            dist(p1, p2),
            dist(p1, p3),
            dist(p1, p4),
            dist(p2, p3),
            dist(p2, p4),
            dist(p3, p4),
        ]
        D.sort()
        
        # D0, D1, D2, D3 are sides which should be equal
        # D4, D5 are diagonals which should be equal
        return True if 0 < D[0] == D[1] == D[2] == D[3] and D[4] == D[5] else False 