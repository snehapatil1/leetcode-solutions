class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-counts[ch] for ch in counts]
        heapq.heapify(heap)
        intervals = 0

        while heap:
            cycle = n + 1
            store = []
            tasks = 0
            while cycle > 0 and heap:
                curr = -heapq.heappop(heap)
                if curr > 1:
                    store.append(-(curr - 1))
                tasks += 1
                cycle -= 1
            for x in store:
                heapq.heappush(heap, x)
            intervals += tasks if not heap else n + 1

        return intervals