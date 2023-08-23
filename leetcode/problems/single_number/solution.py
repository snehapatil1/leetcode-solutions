class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash_map = {}
        # for i in nums:
        #     if i not in hash_map.keys():
        #         hash_map.update({i: 1})
        #     else:
        #         hash_map[i] += 1
        
        # for i in hash_map:
        #     if hash_map[i] == 1:
        #         return i

        # ========== Bit Manipulation

        xor = 0

        for num in nums:
            xor ^= num
        
        return xor