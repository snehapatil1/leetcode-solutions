class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        buckets = [[""] for _ in range(numRows)]
        sPointer = 0
        moveRight = True
        bucket = 0
        while sPointer < len(s):
            if bucket == numRows and moveRight:
                bucket -= 1
                moveRight = False
            if bucket == 0 and not moveRight:
                bucket += 1
                moveRight = True
            
            if moveRight:
                buckets[bucket].append(s[sPointer])
                bucket += 1
            else:
                bucket -= 1
                buckets[bucket].append(s[sPointer])
            sPointer += 1
        
        return "".join([ch for bucket in buckets for ch in bucket])