class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = []
        n = len(rooms)
        vis = [0 for i in range(n)]
        visited = 1
        vis[0] = 1
        for key in rooms[0]:
            q.append(key)
            vis[key] = 1
        while q:
            ind = q.pop(0)
            visited += 1
            for key in rooms[ind]:
                if not vis[key]:
                    q.append(key)
                    vis[key] = 1
        if visited == n:
            return True
        return False
        