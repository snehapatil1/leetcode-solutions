class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        # heap = [(-counts[num], num) for num in counts]
        # heapq.heapify(heap)
        # output = []
        # for i in range(k):
        #     _, num = heapq.heappop(heap)
        #     output.append(num)
        # return output
        return heapq.nlargest(k, counts.keys(), key=counts.get)