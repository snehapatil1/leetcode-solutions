class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def get_next_number(num):
            total = 0
            while num:
                digit = num % 10
                total += digit ** 2
                num = num // 10
            return total
        
        while n not in seen:
            seen.add(n)
            n = get_next_number(n)
            if n == 1:
                return True
        
        return n == 1