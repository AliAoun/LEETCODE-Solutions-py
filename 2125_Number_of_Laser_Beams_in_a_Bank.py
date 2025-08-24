class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = bank[0].count("1")
        res = 0

        for i in range(1, len(bank)):
            cur = bank[i].count("1")
            if cur:
                res += (prev * cur)
                prev = cur
        return res
    
    # time complexity: O(m * n), where m is the number of rows and n is the number of columns in the bank
    # space complexity: O(1) due to the use of a constant amount of extra space