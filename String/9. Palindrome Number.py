class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        x_arr = list(x_str)
        x_arr.reverse()
        x_arr_str = ''.join(x_arr)
        if str(x) == x_arr_str:
            return True
        else:
            return False
