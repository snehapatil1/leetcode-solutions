class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = collections.deque([(startGene, 0)])
        visited = set()
        visited.add(startGene)
        
        while queue:
            temp, count = queue.popleft()
            if temp == endGene:
                return count
            
            for ch in 'ACGT':
                for idx in range(len(temp)):
                    neighbor = temp[:idx] + ch + temp[idx + 1:]
                    if neighbor not in visited and neighbor in bank:
                        queue.append((neighbor, count + 1))
                        visited.add(neighbor)
        
        return -1