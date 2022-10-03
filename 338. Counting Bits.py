class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            tmp = i
            cnt = 0
            while tmp:
                if tmp % 2 == 1:
                    cnt += 1
                tmp = tmp // 2
            ans.append(cnt)
        return ans
        