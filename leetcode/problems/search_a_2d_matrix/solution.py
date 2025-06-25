class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1

        while left <= right:
            mid = (left + right) // 2
            cell = matrix[mid//cols][mid%cols]
            if cell < target:
                left = mid + 1
            elif cell > target:
                right = mid - 1
            else:
                return True
        
        return False