class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = Counter(nums)
        # heap = [(-counts[num], num) for num in counts]
        # heapq.heapify(heap)
        # output = []
        # for i in range(k):
        #     _, num = heapq.heappop(heap)
        #     output.append(num)
        # return output
        # return heapq.nlargest(k, counts.keys(), key=counts.get)

        n = len(nums)
        bucket = [[] for i in range(n + 1)]
        output = []
        counts = Counter(nums)
        
        for key in counts:
            bucket[counts[key]].append(key)
        
        for idx in range(n, -1, -1):
            if len(output) == k:
                break
            
            if bucket[idx]:
                cur = 0
                while cur < len(bucket[idx]) and len(output) < k:
                    output.append(bucket[idx][cur])
                    cur += 1
        
        return output
