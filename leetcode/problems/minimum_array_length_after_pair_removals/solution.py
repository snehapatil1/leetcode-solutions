class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxCount = max([num[1] for num in counts.items()])
        n = len(nums)

        if maxCount <= n / 2:
            if n % 2:
                return 1
            else:
                return 0
        
        return (maxCount*2) - n