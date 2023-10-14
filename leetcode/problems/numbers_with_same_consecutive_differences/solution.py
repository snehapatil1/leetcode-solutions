class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        combinations = []
        queue = deque((1, d) for d in range(1, 10))

        while queue:
            pos, num = queue.pop()
            if pos == n:
                combinations.append(num)
            else:
                for j in range(10):
                    if abs(num % 10 - j) == k:
                        queue.append((pos + 1, num * 10 + j))
        
        return combinations

        # def backtrack(num):
        #     if len(str(num)) == n:
        #         if num not in combinations:
        #             combinations.append(num)
        #         return
            
        #     remaining = num % 10
        #     if remaining + k < 10:
        #         backtrack(num * 10 + (remaining + k))
        #     if remaining - k >= 0:
        #         backtrack(num * 10 + (remaining - k))

        # for i in range(1, 10):
        #     backtrack(i)

        # return combinations