class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict(int)
        for idx, num in enumerate(nums):
            diff = target - num
            if num in hmap:
                return [hmap[num], idx]
            hmap[diff] = idx
