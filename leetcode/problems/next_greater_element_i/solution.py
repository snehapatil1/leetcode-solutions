class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hmap = defaultdict(int)
        output = []

        for num in nums2:
            while stack and num > stack[-1]:
                small = stack.pop()
                hmap[small] = num
            stack.append(num)
        
        while stack:
            small = stack.pop()
            hmap[small] = -1
        
        output = [hmap.get(num, -1) for num in nums1]
        return output
        
        # hmap = defaultdict(int)
        # to_check = []
        # output = [-1] * len(nums1)
        # seen = []

        # for idx, num in enumerate(nums1):
        #     hmap[num] = idx

        # for num in nums2:
        #     if num in hmap:
        #         if num not in to_check:
        #             to_check.append(num)
        #     for n in to_check:
        #         if num > n:
        #             output[hmap[n]] = num
        #             seen.append(n)
        #     for n in seen:
        #         if n in to_check:
        #             to_check.remove(n)
        
        # return output