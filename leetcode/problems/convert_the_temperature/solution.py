class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [round((celsius + 273.15), 5), round((celsius * 1.80 + 32.00), 5)]