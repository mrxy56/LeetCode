class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        height = len(matrix)
        width = len(matrix[0])
        row = height - 1
        col = 0
        while col < width and row >= 0:
            if matrix[row][col] > target: # The order of searching is important.
                row -= 1
            elif matrix[row][col] < target: # Search row first then search col.
                col += 1
            else:
                return True
        return False