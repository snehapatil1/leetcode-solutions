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
