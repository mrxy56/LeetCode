# 1. Use dx, dy as a base, check slope, avoid float number.
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        for i in range(1, n):
            ndx = coordinates[i][0] - coordinates[0][0]
            ndy = coordinates[i][1] - coordinates[0][1]
            if ndx * dy != ndy * dx:
                return False
        return True