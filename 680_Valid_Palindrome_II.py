class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1

        while l < r:
            if s[l] != s[r]:
                moveL, moveR = s[l + 1 : r + 1], s[l : r]
                return moveL == moveL[::-1] or moveR == moveR[::-1]
            l += 1
            r -= 1
        return True
    
    