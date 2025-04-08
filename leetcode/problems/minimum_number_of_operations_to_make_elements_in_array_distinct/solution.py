class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0
        while sum(counts.values()) > len(counts.keys()):
            n = 3 if len(nums) >= 3 else len(nums)

            for i in range(n):
                counts[nums[i]] -= 1
                if not counts[nums[i]]:
                    del counts[nums[i]]
            nums = nums[n:]
            res += 1
        
        return res