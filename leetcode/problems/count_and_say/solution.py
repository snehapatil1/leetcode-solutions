class Solution:
    def countAndSay(self, n: int) -> str:
        def readAndCount(s):
            count = 1
            result = ""

            for i in range(len(s)):
                if i == len(s) - 1:
                    result += f"{count}{s[i]}"
                elif s[i + 1] != s[i]:
                    result += f"{count}{s[i]}"
                    count = 1
                else:
                    count += 1
            
            return result

        if n == 1:
            return "1"
        else:
            say = self.countAndSay(n - 1)
            return readAndCount(say)