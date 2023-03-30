class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        friends = ''.join(map(chr, range(n)))
        for timestamp, person1, person2 in sorted(logs):
            friends = friends.replace(friends[person1], friends[person2])
            if len(set(friends)) == 1:
                return timestamp
        return -1
