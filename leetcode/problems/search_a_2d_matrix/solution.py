class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix):
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        end = (rows * cols) - 1

        while start <= end:
            mid = (start + end) // 2
            cell = matrix[mid//cols][mid%cols]
            if target == cell:
                return True 
            if target < cell:
                end = mid - 1
            else:
                start = mid + 1
        return False