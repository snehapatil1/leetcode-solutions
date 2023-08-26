class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards) == len(set(cards)) or len(cards) == 1:
            return -1
        
        n = len(cards)
        mincards = float('inf')
        counter = defaultdict(tuple)

        for start in range(n):
            if cards[start] not in counter:
                counter[cards[start]] = (1, start)
                continue
            else:
                count, idx = counter[cards[start]]
                mincards = min(mincards, start - idx + 1)
                counter[cards[start]] = (count + 1, start)

        return mincards