class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # visited = []
        # for num in nums:
        #     if num in visited:
        #         return True
        #     visited.append(num)
        # return False

        original_length = len(nums)
        unique_nums_length = len(set(nums))
        if unique_nums_length < original_length:
            return True
        return False
