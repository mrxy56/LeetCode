class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        ans1 = []
        ans2 = []
        ans = []
        for num in nums1:
            if num in s1 and num not in s2:
                ans1.append(num)
        for num in nums2:
            if num in s2 and num not in s1:
                ans2.append(num)
        ans1 = list(set(ans1))
        ans2 = list(set(ans2))
        ans.append(ans1)
        ans.append(ans2)
        return ans