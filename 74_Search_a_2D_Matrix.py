class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = (m * n) - 1

        while low <= high:
            mid = (low + high) // 2
            
            # Convert 1D index to 2D coordinates
            row = mid // n
            col = mid % n

            mid_element = matrix[row][col]

            if mid_element == target:
                return True
            elif mid_element < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False