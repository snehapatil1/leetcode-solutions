class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if not len(trust) and n==1:
            return 1
        
        trusted_by = {val: [] for pair in trust for val in pair}
        
        for pair in trust:
            if pair[1] in trusted_by.keys():
                trusted_by[pair[1]].append(pair[0])
            else:
                trusted_by.update({pair[1]: [pair[0]]})
        
        keys = sorted(list(trusted_by.keys()))
        values = [val for person in trusted_by for val in trusted_by[person]]
        
        for person in trusted_by:
            if sorted(trusted_by[person]) == [k for k in keys if k!=person] and person not in values:
                return person
            
        return -1