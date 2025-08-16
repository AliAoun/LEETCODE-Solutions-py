class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
    
    # time complexity: O(n) due to the single pass through the string.
    # space complexity: O(n) due to the stack used to store characters.