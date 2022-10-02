class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        P = [0]
        for x in nums:
            P.append(P[-1] + x)
        ans = N + 1
        monoq = collections.deque()
        for y, Py in enumerate(P):
            while monoq and Py <= P[monoq[-1]]: # constrain one, the diff must be at least k, so smaller P is better
                monoq.pop()
            
            while monoq and Py - P[monoq[0]] >= k: # constrain two, the interval must be as short as possible, so optimize
                ans = min(ans, y - monoq.popleft())
            
            monoq.append(y)
        return ans if ans < N + 1 else -1