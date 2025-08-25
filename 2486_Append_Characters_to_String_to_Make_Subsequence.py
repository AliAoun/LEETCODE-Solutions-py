class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j
    
    # time complexity: O(n x m) as we are iterating through both strings once
    # space complexity: O(1) as we are using only a constant amount of extra space