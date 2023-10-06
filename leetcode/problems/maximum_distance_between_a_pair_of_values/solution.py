class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxDistance, p1, p2 = 0, 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                maxDistance = max(maxDistance, p2 - p1)
                p2 += 1
            else:
                p1 += 1
                if p1 > p2:
                    p2 += 1
        
        return maxDistance

        
        # nums1Ptr, n = 0, len(nums2) - 1
        # maxDistance = 0

        # for idx, num in enumerate(nums1):
        #     left, right = idx, n
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if num <= nums2[mid]:
        #             maxDistance = max(maxDistance, mid - idx)
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        
        # return maxDistance
            