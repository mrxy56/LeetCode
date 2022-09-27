class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        group = {}
        for tmp in arr:
            cnt = 0
            a = tmp
            while a:
                if a % 2 == 1:
                    cnt += 1
                a = a // 2
            if group.get(cnt):
                group[cnt].append(tmp)
            else:
                group[cnt] = [tmp] # should be [tmp] not []
        ans = []
        for k, v in sorted(group.items()):
            ans += sorted(v)
        return ans