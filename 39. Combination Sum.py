class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = [[] for i in range(target + 1)]
        for i in range(1, target + 1):
            path[i] = []
            for j, c in enumerate(candidates): # complete backpack
                if i - c == 0:
                    path[i].append([c])
                elif i - c > 0 and path[i - c]:
                    for p in path[i - c]: # multiple lists in path
                        path[i].append(p + [c])
        ans = set()
        for p in path[target]: # answers of unique frequency
            p.sort()
            ans.add(tuple(p))
        return list(ans)
    