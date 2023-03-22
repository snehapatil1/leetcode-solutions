class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: idx for idx, ch in enumerate(s)}
        op = []
        start = end = 0

        for idx, ch in enumerate(s):
            end = max(end, last[ch])
            if idx == end:
                op.append(idx + 1 - start)
                start = idx + 1
        
        return op