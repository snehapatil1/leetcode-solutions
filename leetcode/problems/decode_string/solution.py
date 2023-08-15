class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_digit = 0
        cur_string = ''

        for ch in list(s):
            if ch == '[':
                stack.append(cur_string)
                stack.append(cur_digit)
                cur_string = ''
                cur_digit = 0
            elif ch == ']':
                num = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + cur_string * num
            elif ch.isdigit():
                cur_digit = cur_digit * 10 + int(ch)
            else:
                cur_string += ch
        
        return cur_string