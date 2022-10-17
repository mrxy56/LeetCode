class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = []
        for i, n in enumerate(number):
            if n == digit:
                ans.append(number[:i] + number[i + 1:])
        return max(ans)