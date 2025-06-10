class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        counts = Counter()
        res = 0
        for num in nums:
            counts[num] = max(counts[num], counts[k]) + 1
            res = max(res, counts[num] - counts[k])

        return counts[k] + res
