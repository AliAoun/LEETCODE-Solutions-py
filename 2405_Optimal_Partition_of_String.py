class Solution:
    def partitionString(self, s: str) -> int:
        curSet = set()
        res = 1
        for c in s:
            if c in curSet:
                res += 1
                curSet = set()
            curSet.add(c)
        return res
    
    # time complexity: O(n) due to single pass through the string.
    # space complexity: O(1) due to fixed size of the set (at most 26 characters).