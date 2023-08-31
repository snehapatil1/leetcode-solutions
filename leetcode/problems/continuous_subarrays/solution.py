class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        start, end, count = 0, 0, 0
        minHeap, maxHeap = [], []

        while end < len(nums):
            while minHeap and abs(minHeap[0][0] - nums[end]) > 2:
                _, index = heapq.heappop(minHeap)
                start = max(start, index + 1)
            while maxHeap and abs(-maxHeap[0][0] - nums[end]) > 2:
                _, index = heapq.heappop(maxHeap)
                start = max(start, index + 1)
            
            heapq.heappush(minHeap, (nums[end], end))
            heapq.heappush(maxHeap, (-nums[end], end))

            count += (end - start + 1)
            end += 1
        
        return count