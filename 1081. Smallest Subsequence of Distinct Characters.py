# 1. Very similiar to a previous one, but pay attention that mp[ch] should decrease by 1 no matter what happend in this round.
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        from collections import defaultdict
        stack = []
        seen = set()
        mp = defaultdict(int)
        for ch in s:
            mp[ch] += 1
        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
                seen.add(ch)
                mp[ch] -= 1
            else:
                if ch not in seen:
                    while len(stack) and ch < stack[-1] and mp[stack[-1]] > 0:
                        tmp = stack.pop()
                        seen.remove(tmp)
                    stack.append(ch)
                    seen.add(ch)
                mp[ch] -= 1
        return "".join(stack)