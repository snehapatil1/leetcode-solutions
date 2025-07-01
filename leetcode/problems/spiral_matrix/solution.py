class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        output = []
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] == 'V':
                return
            
            output.append(matrix[row][col])
            matrix[row][col] = 'V'
            
            if col + 1 >= row:
                dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row - 1, col)
        
        dfs(0, 0)
        
        return output