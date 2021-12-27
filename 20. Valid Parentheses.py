# Pay attention to the last statement, that we need to deal with the case that there is only one character.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        counter = {}
        counter[')'] = '('
        counter[']'] = '['
        counter['}'] = '{'
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            else:
                if c == '(' or c == '[' or c =='{':
                    stack.append(c)
                else:
                    if counter[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        if len(stack) > 0:
            return False
        return True
