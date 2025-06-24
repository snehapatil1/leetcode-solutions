class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        counts = Counter(nums)
        output = []

        for num in counts:
            buckets[counts[num]].append(num)
        
        for idx in range(len(buckets) - 1, -1, -1):
            if len(output) == k:
                return output
            
            for num in buckets[idx]:
                if len(output) < k:
                    output.append(num)