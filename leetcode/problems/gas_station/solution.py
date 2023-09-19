class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        stations = len(gas)
        startIndex = 0
        totalGas, remainingGas = 0, 0

        for idx in range(stations):
            totalGas += gas[idx] - cost[idx]
            remainingGas += gas[idx] - cost[idx]
            if remainingGas < 0:
                remainingGas = 0
                startIndex = idx + 1
        return startIndex if totalGas >= 0 else -1