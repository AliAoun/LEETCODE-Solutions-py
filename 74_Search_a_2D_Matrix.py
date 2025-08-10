class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            m_row = (top + bot) // 2
            if target > matrix[m_row][-1]:
                top = m_row + 1
            elif target < matrix[m_row][0]:
                bot = m_row - 1
            else:
                break
            
        if not (top <= bot):
            return False
        
        m_row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2 
            if target > matrix[m_row][m]:
                l = m + 1
            elif target < matrix[m_row][m]:
                r = m - 1
            else:
                return True
        return False
    
    # time complexity: O(log(m * n)), where m is the number of rows and n is the number of columns (due to the binary search in both dimensions).
    # space complexity: O(1), as we are using a constant amount of space for variables (due to no additional data structures being used.)