class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = [""] * n

        for i in range(n):
            num = i + 1
            if num % 3 == 0 and num % 5 == 0:
                output[i] = "FizzBuzz"
                continue
            elif num % 3 == 0:
                output[i] = "Fizz"
                continue
            elif num % 5 == 0:
                output[i] = "Buzz"
                continue
            else:
                output[i] = str(num)

        return output