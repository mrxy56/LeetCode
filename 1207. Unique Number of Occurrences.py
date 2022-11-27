class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set()
        mp = {}
        for elem in arr:
            if elem not in mp:
                mp[elem] = 1
            else:
                mp[elem] += 1
        for k, v in mp.items():
            if v in s:
                return False
            s.add(v)
        return True