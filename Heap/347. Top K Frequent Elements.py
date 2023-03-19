import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##### Brute Force Solution #####
        # counts = Counter(nums)
        # indices = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:k]
        # output = [index[0] for index in indices]
        # return output

        ##### Heap Solution #####
        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=counts.get)
