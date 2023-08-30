class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = defaultdict(int)

        for birth, death in logs:
            for year in range(birth, death):
                population[year] += 1
        
        return max(population.items(), key=lambda x: (x[1], -x[0]))[0]