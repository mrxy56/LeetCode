class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        mp1 = {}
        mp2 = {}
        n1 = len(nums1)
        n2 = len(nums2)
        n3 = len(nums3)
        n4 = len(nums4)
        for i in range(n1):
            for j in range(n2):
                if nums1[i] + nums2[j] in mp1:
                    mp1[nums1[i] + nums2[j]] += 1
                else:
                    mp1[nums1[i] + nums2[j]] = 1
                    
        for i in range(n3):
            for j in range(n4):
                if nums3[i] + nums4[j] in mp2:
                    mp2[nums3[i] + nums4[j]] += 1
                else:
                    mp2[nums3[i] + nums4[j]] = 1
                    
        for k1, v1 in mp1.items():
            for k2, v2 in mp2.items():
                if k1 + k2 == 0:
                    ans += v1 * v2
                           
        return ans