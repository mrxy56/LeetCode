class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        R, C = len(isInfected), len(isInfected[0]) # R, C needs to be Capital or else it will mix up.
        def isvalid(nr, nc):
            if nr >= 0 and nr < R and nc >= 0 and nc < C:
                return True
            return False
                    
        def dfs(r, c):
            if (r, c) not in seen:
                seen.add((r, c))
                regions[-1].add((r, c))
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if isvalid(nr, nc):
                        if isInfected[nr][nc] == 1:
                            dfs(nr, nc)
                        elif isInfected[nr][nc] == 0:
                            frontiers[-1].add((nr, nc))
                            perimeters[-1] += 1
        ans = 0
        while True:
            seen = set() # search, change map
            regions = []
            frontiers = []
            perimeters = []
            for r, row in enumerate(isInfected):
                for c, val in enumerate(row):
                    if val == 1 and (r, c) not in seen:
                        regions.append(set())
                        frontiers.append(set())
                        perimeters.append(0)
                        dfs(r, c)
            if not regions:
                break
            ind = frontiers.index(max(frontiers, key = len)) # index function is the key
            ans += perimeters[ind]
            for i, reg in enumerate(regions):
                if i == ind:
                    for r, c in reg:
                        isInfected[r][c] = -1
                else:
                    for r, c in reg:
                        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            if isvalid(nr, nc) and isInfected[nr][nc] == 0:
                                isInfected[nr][nc] = 1
        return ans