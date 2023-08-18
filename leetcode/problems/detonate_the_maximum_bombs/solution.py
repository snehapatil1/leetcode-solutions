class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        detonated_bombs = 0
        number_of_bombs = len(bombs)
        directed_graph = collections.defaultdict(list)
        
        # create a graph
        def create_graph():
            for bomb1 in range(number_of_bombs):
                for bomb2 in range(number_of_bombs):
                    if bomb1 == bomb2:
                        continue
                    
                    x1, y1, r1 = bombs[bomb1]
                    x2, y2, _ = bombs[bomb2]

                    if r1**2 >= (x1 - x2)**2 + (y1 - y2)**2:
                        directed_graph[bomb1].append(bomb2)
            
            return directed_graph
        
        directed_graph = create_graph()
        
        # check for each node using dfs
        def detonate_neighbouring_bombs(bomb, visited):
            visited.add(bomb)
            for bomb_in_range in directed_graph[bomb]:
                if bomb_in_range not in visited:
                    detonate_neighbouring_bombs(bomb_in_range, visited)
            
            return len(visited)
        
        for bomb in range(number_of_bombs):
            visited = set()
            detonated_bombs = max(detonated_bombs, detonate_neighbouring_bombs(bomb, visited))
        
        return detonated_bombs