class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        output = []

        for interval in intervals:
            if output and output[-1][1] >= interval[0]:
                output[-1][1] = max(output[-1][1], interval[1])
            else:
                output.append(interval)

        return output