class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == 'V':
                return
            
            output.append(matrix[i][j])
            matrix[i][j] = 'V'
            
            if j + 1 >= i:
                dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)
        
        dfs(0, 0)
        return output
