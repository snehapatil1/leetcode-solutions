class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [idx, hash_map[complement]]
            hash_map[num] = idx