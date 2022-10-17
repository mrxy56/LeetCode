class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        diff = abs(sum1 - sum2)
        if sum1 > sum2:
            nums1, nums2 = nums2, nums1
        i = 0
        j = len(nums2) - 1
        ans = 0
        if diff == 0: # edge case
            return 0
        while diff:
            if j < 0 and i >= len(nums1):
                break
            if j < 0 or i < len(nums1) and j >= 0 and 6 - nums1[i] > nums2[j] - 1: # two conditions
                diff -= 6 - nums1[i]
                i += 1
            elif i >= len(nums1) or i < len(nums1) and j >= 0 and 6 - nums1[i] <= nums2[j] - 1: # two conditions
                diff -= nums2[j] - 1
                j -= 1
            ans += 1
            if diff <= 0:
                return ans
        return -1