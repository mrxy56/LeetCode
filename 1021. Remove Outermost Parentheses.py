# Deprive the outer parathesis until it is balanced.
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ls = []
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1
            stack.append(ch)
            if left == right:
                n = len(stack)
                ls.append(''.join(stack[1: n - 1]))
                stack = []
        return ''.join(ls)