# 1. Pay attention to the edge case 0.
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mp = {}
        for a in arr:
            if a in mp:
                mp[a] += 1
            else:
                mp[a] = 1
        for a in arr:
            if a != 0:
                if a * 2 in mp:
                    return True
            else:
                if mp[0] >= 2:
                    return True
        return False