class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            total = numbers[p1] + numbers[p2]
            if total < target:
                p1 += 1
            elif total > target:
                p2 -= 1
            else:
                return [p1 + 1, p2 + 1]
        return [-1, -1]