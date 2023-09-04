class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, visited, prevHeight):
            if (row, col) in visited or row < 0 or row >= ROWS or col < 0 or col >= COLS or heights[row][col] < prevHeight:
                return
            
            visited.add((row, col))
            
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
        
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0]) # visit left border
            dfs(row, COLS - 1, atlantic, heights[row][COLS - 1]) #visit right border
        
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col]) # visit top border
            dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col]) # visit bottom border
        
        output = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    output.append([row, col])
        
        return output