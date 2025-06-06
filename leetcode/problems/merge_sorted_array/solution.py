class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = m - 1, n - 1
        for idx in range(n + m - 1, -1, -1):
            if ptr2 < 0:
                break
            if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
                nums1[idx] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[idx] = nums2[ptr2]
                ptr2 -= 1


        