class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        lsum = [0 for i in range(l)]
        rsum = [0 for i in range(l)]
        for i in range(l):
            if i == 0:
                lsum[i] = nums[i]
            else:
                lsum[i] = lsum[i - 1] + nums[i]
        for j in range(l - 1, -1, -1):
            if j == l - 1:
                rsum[j] = nums[j]
            else:
                rsum[j] = rsum[j + 1] + nums[j] 
        if l == 1: # edge case
            return 0
        for i in range(l):
            if i == 0 and rsum[1] == 0:
                return 0
            if i == l - 1 and lsum[l - 2] == 0:
                return l - 1
            if i != 0 and i != l - 1 and lsum[i - 1] == rsum[i + 1]:
                return i
        
        return -1