class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        output = -1

        for h1, h2, m1, m2 in itertools.permutations(arr):
            hour = h1 * 10 + h2
            minutes = m1 * 10 + m2

            if hour <= 23 and minutes <= 59:
                output = max(output, hour * 60 + minutes)
        
        if output == -1:
            return ""
        else:
            hour = output // 60
            minutes = output % 60
            return "{:02d}:{:02d}".format(hour, minutes)