class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        output = defaultdict(int)
        index = 0

        for query in sorted(queries):
            while index < len(intervals) and intervals[index][0] <= query:
                l, r = intervals[index]
                heapq.heappush(minHeap, (r - l + 1, r))
                index += 1
            
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            
            output[query] = minHeap[0][0] if minHeap else -1
        
        return [output[q] for q in queries]