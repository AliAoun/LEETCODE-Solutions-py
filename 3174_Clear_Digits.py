class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        def isdigit(c):
            return ord("0") <= ord(c) <= ord("9")

        for i in range(len(s)):
            if isdigit(s[i]):
                res.pop()
            else:
                res.append(s[i])
        
        return "".join(res)
    
    # time complexity: O(n)
    # space complexity: O(n)