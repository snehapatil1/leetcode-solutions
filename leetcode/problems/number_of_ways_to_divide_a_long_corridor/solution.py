class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        seats, plants, dividers = 0, 0, 1

        for val in corridor:
            if val == 'S':
                seats += 1
            
            if seats == 2 and val == 'P':
                plants += 1

            if seats == 3:
                dividers = (dividers * (plants + 1)) % MOD
                seats = 1
                plants = 0
        
        return 0 if seats < 2 else dividers