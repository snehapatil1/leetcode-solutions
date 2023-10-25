class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = defaultdict(int)

        for idx in range(len(nums)):
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        
        return False