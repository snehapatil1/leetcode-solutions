from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.count = 0
        queue = deque()
        
        def dfs(row, col):
            if grid[row][col] == 1 :
                queue.append((row, col, 0))
                grid[row][col] = 'V'
                if row - 1 >= 0:
                    dfs(row - 1, col)
                if row + 1 < len(grid):
                    dfs(row + 1, col)
                if col - 1 >= 0:
                    dfs(row, col - 1)
                if col + 1 < len(grid):
                    dfs(row, col + 1)
        
        def bfs(queue):
            visited = set()
            while queue:
                r, c, cnt = queue.popleft()
                if grid[r][c] == 1:
                    return cnt
                else:
                    for x, y in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)) :
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) : 
                            if (x, y) not in visited:
                                visited.add((x, y))
                                queue.append((x, y, cnt + 1))
        
        flag = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    flag = True
                    break
            if flag:
                break
    
        return bfs(queue) - 1
