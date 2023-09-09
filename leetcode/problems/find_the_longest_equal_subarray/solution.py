class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        numCounter = defaultdict(int)
        i, maxLen = 0, 0
        
        for j in range(len(nums)):
            numCounter[nums[j]] = numCounter.get(nums[j], 0) + 1
            maxLen = max(maxLen, numCounter[nums[j]])
            if j - i + 1 - maxLen > k:
                numCounter[nums[i]] -= 1
                i += 1
        return maxLen