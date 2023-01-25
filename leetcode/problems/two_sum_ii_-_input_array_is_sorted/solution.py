class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for idx, val in enumerate(numbers):
            a = target - val
            if a in seen:
                return [seen[a]+1, idx+1]
            seen[val] = idx