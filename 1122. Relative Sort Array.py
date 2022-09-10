class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        nq = []
        d = {}
        l = len(arr2)
        for i in range(l):
            d[arr2[i]] = i
        cnt = [0 for i in range(l)]
        for num in arr1:
            if num in d:
                cnt[d[num]] += 1
            else:
                nq.append(num)
        ans = []
        for num in arr2:
            for j in range(cnt[d[num]]):
                ans += [num]
        nq.sort()
        ans += nq
        return ans