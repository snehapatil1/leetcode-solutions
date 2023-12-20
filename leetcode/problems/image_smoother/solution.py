class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])

        for row in range(ROWS):
            for col in range(COLS):
                total, count = 0, 0

                for nrow in (row - 1, row, row + 1):
                    for ncol in (col - 1, col, col + 1):
                        if 0 <= nrow < ROWS and 0 <= ncol < COLS:
                            total += img[nrow][ncol] % 256
                            count += 1
                
                img[row][col] += (total // count) * 256
        
        for row in range(ROWS):
            for col in range(COLS):
                img[row][col] //= 256
            
        return img