class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list) #defaultdict
        for s in strs:
            ans[tuple(sorted(s))].append(s) # tuple can be index
        return ans.values()