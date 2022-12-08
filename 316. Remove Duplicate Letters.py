# 1. Use stack, defaultdict(int).
# 2. Greedy, always subsitute the current one with a potential better solution.
# 3. Use set to track the current selected letters.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import defaultdict
        seen = set()
        stack = []
        mp = defaultdict(int)
        for ch in s:
            mp[ch] += 1
        for ch in s:
            if ch not in seen and mp[ch] > 0:
                if len(stack) == 0:
                    stack.append(ch)
                    seen.add(ch)
                else:
                    while stack and stack[-1] > ch and mp[stack[-1]] > 0:
                        seen.remove(stack[-1])
                        stack.pop()
                    stack.append(ch)
                    seen.add(ch)

            mp[ch] -= 1
        return "".join(stack)