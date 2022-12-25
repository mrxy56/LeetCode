# 1. Pay attention to the condition that there should only be 0s between 1s and -1s.
# 2. Need to think about a quicker solution, this is O(n^3).
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        space = []
        army = []
        n = len(forts)
        vis = [0 for i in range(n)]
        def correct(x, y):
            if x > y:
                x, y = y, x
            for i in range(x + 1, y):
                if forts[i]!= 0:
                    return False
            return True
        
        for i, fort in enumerate(forts):
            if fort == -1:
                space.append(i)
                vis[i] = 2
            elif fort == 1:
                army.append(i)
                vis[i] = 2
        ans = 0
        for a in army:
            for s in space:
                if correct(a, s):
                    ans = max(abs(a - s) - 1, ans)
        return ans