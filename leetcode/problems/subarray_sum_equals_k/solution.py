class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        total, count = 0, 0
        hmap[0] = 1

        for idx in range(len(nums)):
            total += nums[idx]
            if (total - k) in hmap:
                count += hmap[total - k]
            hmap[total] = hmap.get(total, 0) + 1
        
        return count