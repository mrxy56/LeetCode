class Solution:
    def countOdds(self, low: int, high: int) -> int:
        tmp = 0
        if low % 2 == 0:
            low -= 1
            tmp += 1
        if high % 2 == 0:
            high += 1
            tmp += 1
        return (high - low) // 2 + 1 - tmp