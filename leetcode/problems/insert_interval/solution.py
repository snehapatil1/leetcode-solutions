class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.extend([newInterval])
        intervals.sort()
        mergedIntervals = []

        for start, end in intervals:
            if not mergedIntervals:
                mergedIntervals.append([start, end])
                continue
            
            if mergedIntervals[-1][-1] >= start:
                if mergedIntervals[-1][-1] < end:
                    mergedIntervals[-1][-1] = end
            else:
                mergedIntervals.append([start, end])
        
        return mergedIntervals