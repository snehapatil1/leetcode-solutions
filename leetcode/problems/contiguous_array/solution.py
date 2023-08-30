class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n, maxlen, count = len(nums), 0, 0
        prefix_sum = {0: -1}

        for idx, num in enumerate(nums):
            count = count + (1 if num == 1 else -1)
            if count in prefix_sum:
                maxlen = max(maxlen, idx - prefix_sum[count])
            else:
                prefix_sum[count] = idx
        
        return maxlen