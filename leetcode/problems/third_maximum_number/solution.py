import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        heapq.heapify(nums)
        return heapq.nlargest(3, nums)[-1] if len(nums) >= 3 else max(nums)