class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        hset = {num : 1 for num in arr}

        for num1 in arr:
            for num2 in arr:
                if num1 == num2:
                    break
                if num1 % num2 == 0 and num1 // num2 in hset:
                    hset[num1] += hset[num2] * hset[num1 // num2]
        
        return sum(hset.values()) % MOD