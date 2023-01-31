class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash_map = {}
        count = 0
        temp = [num for num in nums]

        for idx, num in enumerate(temp):
            if num in hash_map:
                hash_map[num] += 1
                nums.remove(num)
                nums.append('_')
            else:
                hash_map[num] = 1
                count += 1
