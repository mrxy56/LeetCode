class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stack = []
        ans = []
        
        for x in nums2:
            while(stack and x > stack[-1]):
                mp[stack.pop()] = x
            stack.append(x)

        for x in nums1:
            ans.append(mp.get(x, -1))
            
        return ans