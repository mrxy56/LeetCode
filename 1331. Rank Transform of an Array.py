class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        narr = list(set(arr))
        narr.sort()
        d = {}
        for i, a in enumerate(narr):
            d[a] = i + 1
        ans = []
        for a in arr:
            ans.append(d[a])
        return ans