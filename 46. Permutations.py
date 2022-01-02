class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        vis = [0 for i in range(n)]
        def dfs(nums, vis, ls):
            if len(ls) == n:
                ans.append(ls)
            for i in range(n):
                if vis[i] == 0:
                    vis[i] = 1
                    dfs(nums, vis, ls + [nums[i]])
                    vis[i] = 0
                else:
                    continue
        dfs(nums, vis, [])
        return ans