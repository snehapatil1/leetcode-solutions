class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        output = 0
        
        for val in counts:
            if counts[val] == 1:
                return -1
            output += ceil(counts[val] / 3)
        
        return output