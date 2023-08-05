"""
    Question:
        An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
        You are also given three integers sr, sc, and color. 
        You should perform a flood fill on the image starting from the pixel image[sr][sc].
        To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the 
        same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
        Replace the color of all of the aforementioned pixels with color.
        Return the modified image after performing the flood fill.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # if the cell is already visited and is colored then that's the end of possible coloring hence return the image
        if image[sr][sc] == color:
            return image
        
        self.fill(image, sr, sc, color, image[sr][sc])
        
        return image
    
    def fill(self, image, sr, sc, color, cur):
        # if the row or column doesn't exist as per matrix size then return
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        
        # if current cel value is not same as desired value then no need to cover borders of that cell hence return
        if cur != image[sr][sc]:
            return
        
        # set current cell to color value
        image[sr][sc] = color
        
        # cover immediate top cell
        self.fill(image, sr-1, sc, color, cur)
        # cover immediate bottom cell
        self.fill(image, sr+1, sc, color, cur)
        # cover immediate left cell
        self.fill(image, sr, sc-1, color, cur)
        # cover immediate right cell
        self.fill(image, sr, sc+1, color, cur)
