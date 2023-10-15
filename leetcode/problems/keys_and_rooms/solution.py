class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        graph = defaultdict(list)

        for src, dest in enumerate(rooms):
            graph[src].extend(dest)
        
        queue = deque([0])
        visited = set()

        while queue:
            room = queue.popleft()
            visited.add(room)
            for nextRoom in graph[room]:
                if nextRoom not in visited:
                    queue.append(nextRoom)
        
        return len(visited) == n