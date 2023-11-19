class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        tmp = ans = 0
        for g in gain:
            tmp += g
            if tmp > ans:
                ans = tmp
        return ans