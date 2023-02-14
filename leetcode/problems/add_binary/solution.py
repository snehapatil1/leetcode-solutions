class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_arr = list(a)
        b_arr = list(b)
        a_arr_int = [int(ele) for ele in a_arr]
        b_arr_int = [int(ele) for ele in b_arr]
        new_reversed_arr = []
        a_len = len(a_arr_int)
        b_len = len(b_arr_int)
        arr_len = max(a_len, b_len)

        if a_len != b_len:
            if a_len > b_len:
                diff = a_len - b_len
                old_b_arr_int = b_arr_int
                b_arr_int = []
                while diff > 0:
                    b_arr_int.append(0)
                    diff -= 1
                b_arr_int.extend(old_b_arr_int)
            if b_len > a_len:
                diff = b_len - a_len
                old_a_arr_int = a_arr_int
                a_arr_int = []
                while diff > 0:
                    a_arr_int.append(0)
                    diff -= 1
                a_arr_int.extend(old_a_arr_int)
        
        carry_forward = 0

        # print(a_arr_int, b_arr_int)
        
        i = arr_len - 1
        while i < arr_len and i >= 0:
            if i < len(a_arr_int):
                ele1 = a_arr_int[i]
            else:
                ele1 = 0
            
            if i < len(b_arr_int):
                ele2 = b_arr_int[i]
            else:
                ele2 = 0
            
            # print(ele1, ele2)
            current_val = ele1 + ele2 + carry_forward
            if current_val == 3:
                val = 1
                carry_forward = 1
            elif current_val == 2:
                val = 0
                carry_forward = 1
            else:
                val = current_val
                carry_forward = 0
            new_reversed_arr.append(val)
            # print('else', new_reversed_arr, carry_forward)
        
            i -= 1

        # print(new_reversed_arr, carry_forward)
        if carry_forward:
            new_reversed_arr.append(carry_forward)
        
        new_reversed_arr.reverse()
        new_correct_arr_str = [str(ele) for ele in new_reversed_arr]
        return "".join(new_correct_arr_str)
            
