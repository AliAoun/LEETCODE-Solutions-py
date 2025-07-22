class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        res = []

        def btrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitMap[digits[i]]:
                btrack(i + 1, curStr + c)
        
        if digits:
            btrack(0, "")
        return res