class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        nums1_index, nums2_index = 0, 0
        for write_index in range(m + n):
            if nums2_index >= n or (nums1_index < m and temp[nums1_index] < nums2[nums2_index]):
                nums1[write_index] = temp[nums1_index]
                nums1_index += 1
            else:
                nums1[write_index] = nums2[nums2_index]
                nums2_index += 1