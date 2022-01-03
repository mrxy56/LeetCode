class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m, n = len(bank), len(bank[0])
        nums = [0 for i in range(m)]
        for i in range(m):
            for j in range(n):
                if bank[i][j] == '1':
                    nums[i] += 1
        ans = 0
        flag = False
        last = 0
        for i in range(m):
            if nums[i] > 0:
                if flag:
                    ans += last * nums[i]
                flag = True
                last = nums[i]
        return ans