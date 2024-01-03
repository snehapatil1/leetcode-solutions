class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev, lasers = 0, 0

        for row in bank:
            if nxt:= row.count('1'):
                lasers += (prev * nxt)
                prev = nxt
        
        return lasers