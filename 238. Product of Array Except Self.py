class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lp = [0 for i in range(l)] # Calculate left part and right part production
        rp = [0 for i in range(l)]
        lp[0] = nums[0]
        rp[-1] = nums[-1]
        for i in range(1, l):
            lp[i] = lp[i - 1] * nums[i]
        for j in range(l - 1, 0, -1):
            rp[j - 1] = rp[j] * nums[j - 1]
        ans = []
        for i in range(l):
            if i == 0:
                ans.append(rp[1])
            elif i == l - 1:
                ans.append(lp[l - 2])
            else:
                ans.append(lp[i - 1] * rp[i + 1])
        return ans