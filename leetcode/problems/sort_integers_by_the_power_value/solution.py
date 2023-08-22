from sortedcontainers import SortedDict
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}

        @cache
        def get_power(num):
            if num in memo:
                return memo[num]
            if num % 2 == 0:
                new_num = int(num / 2)
            else:
                new_num = int((num * 3) + 1)
            
            n = memo[num] = get_power(new_num) + 1
            return n
        
        final_list = [(get_power(num), num) for num in range(lo, hi + 1)]
        return sorted(final_list)[k - 1][1]