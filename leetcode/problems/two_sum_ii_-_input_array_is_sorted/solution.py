class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # visited = defaultdict(int)

        # for idx in range(len(numbers)):
        #     complement = target - numbers[idx]
        #     if complement in visited:
        #         return [visited[complement] + 1, idx + 1]
        #     visited[numbers[idx]] = idx

        n = len(numbers)
        p1, p2 = 0, n - 1

        while p1 < p2 < n:
            total = numbers[p1] + numbers[p2]
            if total == target:
                return [p1 + 1, p2 + 1]
            if total < target:
                p1 += 1
            else:
                p2 -= 1
        