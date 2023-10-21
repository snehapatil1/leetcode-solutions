class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        output = nums[0]
        heap = [(-nums[0], 0)]
        heapq.heapify(heap)

        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heapq.heappop(heap)
            prev = -heap[0][0]
            curr = nums[i] + (0 if prev < 0 else prev)
            output = max(output, curr)
            heapq.heappush(heap, (-curr, i))
        
        return output