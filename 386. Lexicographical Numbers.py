class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n + 1):
            ans.append(str(i))
        ans.sort()
        for i in range(1, n + 1):
            ans[i - 1] = int(ans[i - 1])
        return ans