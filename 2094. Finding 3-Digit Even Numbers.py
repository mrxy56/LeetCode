class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        s = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        if num // 100 > 0 and num % 2 == 0:
                            s.add(num)
        ans = list(s)
        return sorted(ans)
