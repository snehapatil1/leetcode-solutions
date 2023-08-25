class Solution:
    def compress(self, chars: List[str]) -> int:
        write_pointer, read_pointer = 0, 0

        while read_pointer < len(chars):
            chars[write_pointer] = chars[read_pointer]
            count = 1

            while read_pointer + 1 < len(chars) and chars[read_pointer] == chars[read_pointer + 1]:
                read_pointer += 1
                count += 1
            
            if count > 1:
                for cnt in str(count):
                    chars[write_pointer + 1] = cnt
                    write_pointer += 1
            write_pointer += 1
            read_pointer += 1
        
        return write_pointer