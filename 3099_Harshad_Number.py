class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sn = str(x)
        lst = []
        for c in sn:
            lst.append(int(c))
        if x % sum(lst) == 0:
            return sum(lst)
        else:
            return -1

        # sum_of_digits = 0
        # for digit in str(x):
        #     sum_of_digits += int(digit)

        # if x % sum_of_digits == 0:
        #     return sum_of_digits
        # else:
        #     return -1
        