class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        if color == original_color:
            return image
        
        def helper(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or image[row][col] != original_color:
                return
            
            image[row][col] = color

            helper(row + 1, col)
            helper(row - 1, col)
            helper(row, col + 1)
            helper(row, col - 1)
        
        helper(sr, sc)
        return image