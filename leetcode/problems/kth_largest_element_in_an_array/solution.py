import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ##### Heap Solution #####
        # initialise max heap
        maxHeap = []

        for num in nums:
            # add number in max heap with - value to convert it to a max heap
            heapq.heappush(maxHeap, -num)
        
        # since we want kth largest element, pop ele from max heap till top k-1 element
        while k-1 > 0:
            heapq.heappop(maxHeap)
            k -= 1
        
        # convert -ve to +ve and return top element from the max heap
        return -(heapq.heappop(maxHeap))

        ##### Simple Solution #####
        # nums.sort(reverse=True)
        # return nums[k - 1]

        ##### Heap nlargest Solution #####
        # return heapq.nlargest(k, nums)[-1]