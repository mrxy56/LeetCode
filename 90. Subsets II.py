class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        def dfs(cur, i):
            if i == l:
                ans.append(sorted(cur)) # It must be sorted, or else [1, 4, 4, 4], [4, 4, 1, 4] are considered different.
                return
            dfs(cur, i + 1)
            dfs(cur + [nums[i]], i + 1)
        dfs([], 0)
        s = set()
        for a in ans:
            s.add(tuple(a))
        return sorted(list(s))