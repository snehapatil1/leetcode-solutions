class Solution:
    def reorganizeString(self, s: str) -> str:
        output = ""
        counts = Counter(s)
        heap = [(-val, ch) for ch, val in counts.items()]
        heapq.heapify(heap)

        while heap:
            first_cnt, first_ch = heapq.heappop(heap)
            if not output or output[-1] != first_ch:
                output += first_ch
                if first_cnt + 1 != 0:
                    heapq.heappush(heap, (first_cnt + 1, first_ch))
            else:
                if not heap:
                    return ""
                second_cnt, second_ch = heapq.heappop(heap)
                output += second_ch
                if second_cnt + 1 != 0:
                    heapq.heappush(heap, (second_cnt + 1, second_ch))
                heapq.heappush(heap, (first_cnt, first_ch))

        return output