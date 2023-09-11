class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupMap = defaultdict(list)
        groups = []

        for person, group in enumerate(groupSizes):
            if group not in groupMap:
                groupMap[group] = []
            if len(groupMap[group]) == group:
                groups.append(groupMap[group])
                groupMap[group] = []
            groupMap[group].append(person)
        
        for group in groupMap:
            if groupMap[group] != []:
                groups.append(groupMap[group])
        
        return groups