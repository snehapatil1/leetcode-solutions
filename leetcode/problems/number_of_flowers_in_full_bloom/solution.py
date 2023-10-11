class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        output, starts, ends = [], [], []
        
        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)
        
        starts.sort()
        ends.sort()

        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            output.append(i - j)

        return output