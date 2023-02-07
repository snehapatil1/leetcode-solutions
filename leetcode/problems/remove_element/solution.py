class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)

        while val in nums:
            nums.remove(val)
        
        for i in range(count):
            nums.append('_')
        
        return (len(nums) - count)