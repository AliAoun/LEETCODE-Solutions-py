class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        maxF = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
    
    # time complexity: O(n)
    # space complexity: O(1)