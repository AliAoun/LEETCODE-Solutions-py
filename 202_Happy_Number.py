class Solution:
    def isHappy(self, n: int) -> bool:
        track = set()

        while n not in track:
            track.add(n)
            n = self.sumOfSq(n)
            if n == 1:
                return True
        
        return False

    def sumOfSq(self, n: int) -> int:
        total = 0
        while n:
            digit = n % 10
            total += digit**2
            n = n // 10
        return total
            