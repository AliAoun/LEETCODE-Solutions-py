class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for n in operations:
            if n == "++X" or n == "X++":
                X += 1
            else:
                X -= 1
        return X
    
    # time complexity: O(n)
    # space complexity: O(1)