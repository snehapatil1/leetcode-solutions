class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdegree = defaultdict(int)
        nodes = set()

        for src, dest in paths:
            outdegree[src] = outdegree.get(src, 0) + 1
            nodes.add(src)
            nodes.add(dest)
        
        for node in nodes:
            if outdegree[node] == 0:
                return node
        
        return ""

        # nodes = set([path[0] for path in paths])
        # for path in paths:
        #     if path[1] not in nodes:
        #         return path[1]