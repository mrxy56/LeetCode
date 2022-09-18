class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        vis = [0 for i in range(l)]
        ret = []
        def dfs(layer, ans):
            if layer == l:
                ret.append(ans[:]) # ans is pointer, ans[:] is copy
            for i, num in enumerate(nums): # backtracking
                if not vis[i]:
                    vis[i] = 1
                    dfs(layer + 1, ans + [num])
                    vis[i] = 0
        dfs(0, [])
        S = set()
        for r in ret:
            S.add(tuple(r))
        return list(S)