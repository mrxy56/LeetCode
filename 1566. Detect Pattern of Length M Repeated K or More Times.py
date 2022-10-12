class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n):
            cnt = 1
            if i + m > n: # pay attention to = because of super end
                break
            pattern = arr[i: i + m]
            for j in range(i + m, n, m):
                if j + m <= n and pattern == arr[j: j + m]: # should be <= since we need super end
                    cnt += 1
                else:
                    break
            if cnt >= k:
                return True
        return False