class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k = celsius + 273.15
        f = celsius * 1.8 + 32
        return [k, f]