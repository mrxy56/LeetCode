class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = len(nums)
        def dfs(i, cur):
            ans.append(deepcopy(cur)) # You cannot add cur, since cur is a pointer, finally it will all becomes []
            for j in range(i, l):
                cur.append(nums[j])
                dfs(j + 1, cur)
                cur.pop()
        dfs(0, [])
        return ans
