class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row // 3, col // 3)]:
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        
        return True
        
        # ROWS, COLS = len(board), len(board[0])
        # subBoards = [[2, 2], [2, 5], [2, 8], [5, 2], [5, 5], [5, 8], [8, 2], [8, 5], [8, 8]]

        # def isValidRow(row, col):
        #     if board[row][col] in [board[row][c] for c in range(COLS) if c != col and board[row][c] != "."]:
        #         return False
        #     return True
        
        # def isValidCol(row, col):
        #     if board[row][col] in [board[r][col] for r in range(ROWS) if r != row and board[r][col] != "."]:
        #         return False
        #     return True
        
        # def getSubBoard(row, col):
        #     for subBoard in subBoards:
        #         if row <= subBoard[0] and col <= subBoard[1]:
        #             return subBoard
        
        # def isValidSubBoard(row, col):
        #     subBoard = getSubBoard(row, col)
        #     flattenedBoard = []
        #     for r in range(subBoard[0] - 2, subBoard[0] + 1):
        #         for c in range(subBoard[1] - 2, subBoard[1] + 1):
        #             if r != row and c != col and board[r][c] != ".":
        #                 flattenedBoard.append(board[r][c])
        #     if board[row][col] in flattenedBoard:
        #         return False
        #     return True
        
        # def isValidCell(row, col):
        #     if isValidRow(row, col) and isValidCol(row, col) and isValidSubBoard(row, col):
        #         return True
        #     return False
        
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if board[row][col] != ".":
        #             if not isValidCell(row, col):
        #                 return False
        
        # return True