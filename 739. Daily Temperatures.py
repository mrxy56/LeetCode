# 1. Monotonic Stack, notice that stack.append should be outside of the while loop.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0 for i in range(n)]
        stack = []
        for i in range(n):
            if not stack or (stack and temperatures[i] <= stack[-1][1]):
                stack.append((i, temperatures[i]))
            else:
                while (stack and temperatures[i] > stack[-1][1]):
                    ans[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append((i, temperatures[i]))
        return ans