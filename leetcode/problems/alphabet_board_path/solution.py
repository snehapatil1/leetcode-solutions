class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        mapping = {ch: (idx // 5, idx % 5) for idx, ch in enumerate(ascii_lowercase)}
        path = ''
        row, col = 0, 0

        for ch in target:
            r, c = mapping[ch]

            if c < col:
                path += 'L' * (col - c)
            if r < row:
                path += 'U' * (row - r)
            if r > row:
                path += 'D' * (r - row)
            if c > col:
                path += 'R' * (c - col)
            path += '!'
            row, col = r, c
        
        return path