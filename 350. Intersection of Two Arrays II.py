class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        ans = []
        for num in nums2:
            if num not in mp:
                mp[num] = 1
            else:
                mp[num] += 1

        for num in nums1:
            if num in mp and mp[num] > 0:
                ans.append(num)
                mp[num] -= 1
        return ans