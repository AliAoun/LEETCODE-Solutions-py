class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        countBalloon = Counter("balloon")

        res = len(text)
        
        for c in countBalloon:
            res = min(res, countText[c] // countBalloon[c])
        return res
    
    # time complexity: O(n)
    # space complexity: O(1)