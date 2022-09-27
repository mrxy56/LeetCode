class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        flag = False
        for i in range(l - 1, 0, -1):
            if nums[i] > nums[i - 1]: # find the first ascending pair
                tmp = 100
                tj = -1
                for j in range(i, l):
                    if nums[j] > nums[i - 1]: # find the item which is just larger that nums[i - 1]
                        tmp = min(tmp, nums[j])
                        tj = j
                if tj >= 0:
                    nums[i - 1], nums[tj] = nums[tj], nums[i - 1]
                    for k in range(i, l):
                        for h in range(i + 1, l):
                            if k < h and nums[k] > nums[h]: # sort
                                nums[k], nums[h] = nums[h], nums[k]
                    flag = True
                    break
        if not flag: # edge case of totally descending
            nums.sort()
        return nums
        