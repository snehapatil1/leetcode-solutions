class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        index_map = {idx: val for idx, val in enumerate(nums)}

        for i in range(len(nums)):
            index = i - k
            while index < 0:
                index = len(nums) + index
            nums[i] = index_map[index]
