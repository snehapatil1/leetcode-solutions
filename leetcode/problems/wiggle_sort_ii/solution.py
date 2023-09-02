class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums) + 1) // 2
        small = nums[:mid]
        small.reverse()
        big = nums[mid:]
        big.reverse()
        s, b = 0, 0
        for idx in range(len(nums)):
            if idx % 2 == 0:
                nums[idx] = small[s]
                s += 1
            else:
                nums[idx] = big[b]
                b += 1