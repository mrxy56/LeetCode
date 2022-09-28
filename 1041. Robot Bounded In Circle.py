class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        idx = 0
        
        for i in instructions:
            if i == 'L':
                idx = (idx + 3) % 4
            elif i == 'R':
                idx = (idx + 1) % 4
            else:
                x += d[idx][0]
                y += d[idx][1]
        
        if x == 0 and y == 0 or idx != 0: # if goes back or does not face north, proof is hard, remember it.
            return True
        return False