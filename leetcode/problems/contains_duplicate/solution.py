class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if counts[num] > 1:
                return True
        return False