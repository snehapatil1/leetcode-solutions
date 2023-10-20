class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subarray = []

        for num in nums:
            i = bisect_left(subarray, num)
            if i == len(subarray):
                subarray.append(num)
            else:
                subarray[i] = num
        
        return len(subarray)