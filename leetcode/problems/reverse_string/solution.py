class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not len(s)>0:
            return s
        def recursion(start, end, s):
            if (start == end) or (start < 0) or (end > len(s)) or (start > end):
                return
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -=1
            recursion(start, end, s)
        
        recursion(0, len(s)-1, s)