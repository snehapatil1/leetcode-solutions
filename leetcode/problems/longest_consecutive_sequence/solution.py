class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hash Set
        nums = set(nums)
        maxLen = 0

        for num in nums:
            if num - 1 not in nums:
                length = 1
                while (num + length) in nums:
                    length += 1
                maxLen = max(maxLen, length)
        return maxLen
        
        # Sorting
        # if not nums:
        #     return 0
        # nums = list(set(nums))
        # nums.sort()
        # hmap = defaultdict(int)
        # prev = float('inf')
        # for num in nums:
        #     if num - 1 != prev:
        #         hmap[num] = 1
        #         start = num
        #     else:
        #         hmap[start] += 1
        #     prev = num
        # return max(hmap.values())