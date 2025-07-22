class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = abs(dividend)
        b = abs(divisor)
        negative = (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0)
        output = 0
        
        if (dividend == -2147483648 and divisor == -1):
            return 2147483647

        while a >= b:
            counter = 1
            decrement = b
            while a >= decrement:
                a -= decrement
                output += counter
                counter += counter
                decrement += decrement
        output = output if not negative else -output
        return min(max(-2147483648, output), 2147483648)
            