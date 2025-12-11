class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''

        while columnNumber > 0:
            columnNumber -= 1
            res = chr(columnNumber % 26 + ord('A')) + res 
            columnNumber = columnNumber // 26

        return res  
    
    # Time Complexity: O(N) where N is the number of digits in the resulting title
    # Space Complexity: O(1) due to constant space usage