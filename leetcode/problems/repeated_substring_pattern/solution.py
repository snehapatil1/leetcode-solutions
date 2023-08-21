class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # ========== Brute Force ========== Passes 79 test cases
        # rotated_string = collections.deque(list(s))

        # for i in range(len(s) - 1):
        #     rotated_string.rotate(1)
        #     new_s = "".join(rotated_string)
        #     if new_s == s:
        #         return True
        # return False

        temp = s + s
        if s in temp[1:-1]:
            return True
        return False
