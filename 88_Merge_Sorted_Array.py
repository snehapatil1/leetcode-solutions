class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in reversed(range(m, len(nums1))):
            if nums1[i] == 0:
                nums1.pop(i)
            
        for i in range(0, n):
            nums1.append(nums2[i])
       
        nums1.sort()
