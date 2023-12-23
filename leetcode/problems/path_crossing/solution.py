class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x, y = 0, 0
        visited.add((x, y))

        directions = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }

        for direction in path:
            x += directions[direction][0]
            y += directions[direction][1]
            
            if (x, y) in visited:
                return True
            
            visited.add((x, y))
        
        return False