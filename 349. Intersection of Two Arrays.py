class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        mp = {}
        for num in nums1:
            if not num in mp:
                mp[num] = 1
        for num in nums2:
            if num in mp:
                ans.append(num)
        return set(ans)