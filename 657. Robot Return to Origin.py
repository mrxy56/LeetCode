class Solution:
    def judgeCircle(self, moves: str) -> bool:
        def change(x, y, mode):
            nx = x
            ny = y
            if mode == 'U':
                nx -= 1
            elif mode == 'D':
                nx += 1
            elif mode == 'L':
                ny -= 1
            elif mode == 'R':
                ny += 1
            return nx, ny
        x = 0
        y = 0
        for move in moves:
            x, y = change(x, y, move)
        if x == 0 and y == 0:
            return True
        return False