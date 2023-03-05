class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        missing_ranges = []

        def helper_function(a, b):
            if a + 2 == b:
                missing_ranges.append(f'{a + 1}')
            else:
                missing_ranges.append(f'{a + 1}->{b - 1}')

        nums = [lower - 1] + nums + [upper + 1]
        
        for idx in range(1, len(nums)):
            cur, prev = nums[idx], nums[idx-1]
            if cur - prev > 1:
                helper_function(prev, cur)

        return missing_ranges