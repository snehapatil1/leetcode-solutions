import string
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # set of equal characters
        # find root of character amongst all parents for that character
        def find(ch):
            if parents[ch] == ch:
                return ch
            parents[ch] = find(parents[ch])
            return parents[ch]
        
        # make a dict of all parents from a to z
        parents = {ch: ch for ch in string.ascii_lowercase}
        
        # for each equation - if it is == then group these 2 characters together
        for a, eq, _, b in equations:
            if eq == "=":
                parents[find(a)] = find(b)
        
        # for each equation - if it is != then if their parents are equal the return false
        for a, eq, _, b in equations:
            if eq == "!" and parents[find(a)] == parents[find(b)]:
                return False
        
        return True