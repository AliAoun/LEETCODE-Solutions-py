class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = defaultdict(int)
        for c in magazine:
            d[c] += 1
        for c in ransomNote:
            if c not in d or d[c] <= 0:
                return False
            d[c] -= 1
        return True 

    # time complexity: O(n + m) where n is the length of ransomNote and m is the length of magazine
    # space complexity: O(1) since the dictionary size is limited to the number of unique characters (constant space for lowercase letters)