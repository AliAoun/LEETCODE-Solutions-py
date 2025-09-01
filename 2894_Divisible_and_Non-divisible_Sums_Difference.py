class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for i in range(1, n + 1):
            if i % m == 0:
                num2 = num2 + i
            else:
                num1 = num1 + i
        return num1 - num2

    # time complexity: O(n) as we iterate through numbers from 1 to n once.
    # space complexity: O(1) as we use a constant amount of space.