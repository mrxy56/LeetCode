# 1. In BFS, once added to the queue, marked in vis.
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = []
        vis = set()
        direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        n, m = len(rooms), len(rooms[0])
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
                    vis.add((i, j))
        while q:
            x, y, z = q.pop(0)
            rooms[x][y] = z
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if (nx, ny) not in vis and rooms[nx][ny] != -1:
                        q.append((nx, ny, z + 1))
                        vis.add((nx, ny))
        return rooms
                        
            