class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, -num)
        
        # while k > 0:
        #     num = heapq.heappop(heap)
        #     k -= 1
        
        # return -num

        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1
        
        for num in range(len(count) - 1, -1, -1):
            k -= count[num]
            if k <= 0:
                return min_value + num
        
        return -1