# 1. Sort + Stack.
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        n = len(arr)
        minimum = arr[n - 1] - arr[0]
        for i in range(n - 1):
            if arr[i + 1] - arr[i] < minimum:
                minimum = arr[i + 1] - arr[i]
                while len(ans) and ans[-1][1] - ans[-1][0] > minimum:
                    ans.pop()
                ans.append([arr[i], arr[i + 1]])
            elif arr[i + 1] - arr[i] == minimum:
                ans.append([arr[i], arr[i + 1]])
        return ans