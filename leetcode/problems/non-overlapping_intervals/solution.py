class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last_end = intervals[0][1]
        operations = 0

        for start, end in intervals[1:]:
            if start >= last_end:
                last_end = end
            else:
                operations += 1
                last_end = min(last_end, end)
        
        return operations