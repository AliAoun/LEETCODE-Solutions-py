class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
# ##### 1st Solution with Time = O(n) & Memory = O(1)
#         l = 0
#         r = len(s) - 1

#         while 1 < r:
#             s[l], s[r] = s[r], s[l]
#             l, r = l + 1, r - 1

##### 2nd Solution with Time = O(n) & Space = O(n)

        stack = []
        for c in s:
            stack.append(c)
        
        i = 0 
        while stack:
            s[i] = stack.pop()
            i +=1

##### 3rd Solution with Time = O(n) & Space = O(n)
#         def reverse(l, r):
#             if l < r:
#                 s[l], s[r] = s[r], s[l]
#                 reverse(l + 1, r - 1)
#         reverse(0, len(s) - 1)