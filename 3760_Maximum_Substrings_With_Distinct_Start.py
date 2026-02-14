class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))

    # Time Complexity: O(n) due to conversion of string to set
    # Space Complexity: O(n) in the worst case when all characters are distinct, otherwise O(1) if there are limited distinct characters
