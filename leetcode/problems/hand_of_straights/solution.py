class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        
        hand.sort()
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            val = heap[0]
            for i in range(val, val + groupSize):
                if val not in count:
                    return False
                if count[i] > 0:
                    count[i] -= 1
                    if count[i] == 0:
                        heapq.heappop(heap)
                else:
                    return False

        return True