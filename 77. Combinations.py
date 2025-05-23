class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        vis = [0 for i in range(n + 1)]
        ans = []
        def dfs(num, last, ls):
            if num > k:
                return
            if num == k:
                ans.append(list(ls))
            for i in range(1, n + 1):
                if i > last and not vis[i]:
                    vis[i] = 1
                    dfs(num + 1, i, ls + [i])
                    vis[i] = 0
            return 
        dfs(0, 0, [])
        return ans