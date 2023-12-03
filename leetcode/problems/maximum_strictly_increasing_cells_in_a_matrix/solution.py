class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        maxCells = -float('inf')
        ROWS, COLS = len(mat), len(mat[0])
        cellMap = defaultdict(list)

        for row in range(ROWS):
            for col in range(COLS):
                cellMap[mat[row][col]].append([row, col])
        
        row = [0] * ROWS
        col = [0] * COLS
        
        for ele in sorted(cellMap):
            temp = {}
            
            for r, c in cellMap[ele]:
                maxVal = max(row[r], col[c]) + 1
                temp[(r, c)] = maxVal
                maxCells = max(maxCells, maxVal)
            
            for r, c in cellMap[ele]:
                row[r] = max(row[r], temp[(r, c)])
                col[c] = max(col[c], temp[(r, c)])

        return maxCells