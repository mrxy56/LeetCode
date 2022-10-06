class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        n = len(candidates)
        bits = [0 for i in range(28)]
        for candidate in candidates:
            i = 0
            tmp = candidate
            while tmp:
                bits[i] += tmp & 1 # Theory of bit operations
                tmp = tmp >> 1
                i += 1
        return max(bits) # max function is convenient