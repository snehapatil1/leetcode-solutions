class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(1, n + 1):
            output[i] = output[i & (i - 1)] + 1
        return output
