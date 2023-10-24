class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        i = 0
        ans = []

        while num > 0:
            n = num % 10
            if 1 <= n <= 3:
                ans.append(ones[i] * n) 
            elif n == 4:
                ans.append(ones[i] + fives[i])
            elif 5 <= n <= 8:
                ans.append(fives[i] + ones[i] * (n - 5))
            elif n == 9:
                ans.append(ones[i] + ones[i+1])

            i += 1
            num //= 10

        return "".join(ans[::-1])