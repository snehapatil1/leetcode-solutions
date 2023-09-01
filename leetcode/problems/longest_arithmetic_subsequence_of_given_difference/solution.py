class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        subsequenceLengthMap = defaultdict(int)
        maxLen = 0

        for num in arr:
            prev = subsequenceLengthMap.get(num - difference, 0)
            subsequenceLengthMap[num] = prev + 1
            maxLen = max(maxLen, subsequenceLengthMap[num])
        
        return maxLen