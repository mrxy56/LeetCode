class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        prev = '#'
        i = 0
        while i < len(s):
            if s[i] != prev or len(stack) == 0:
                stack.append(1)
            else:
                stack[-1] += 1
            if stack[-1] == k:
                stack.pop()
                s = s[:i - k + 1] + (s[i + 1:] if i + 1 < len(s) else '')
                i -= k
            if i == -1:
                prev = '#' # using stack to make it easy, pay attention to i == -1.
            else:
                prev = s[i]
            i += 1
        return s