from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return counts.most_common()[0][0]
