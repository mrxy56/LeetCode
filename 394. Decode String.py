# 1. When meet '[', add the prev, add the digit.
# 2. Remember cur is always the most inner string.
# 3. When meet ']', pop and do some calculation, make a new cur.
# 4. Finally cur is the answer.
class Solution:
    def decodeString(self, s: str) -> str:
        stack1 = []
        stack2 = []
        cur = ""
        n = len(s)
        i = 0
        tmp = 0
        while i < n:
            if s[i].isdigit():
                tmp = tmp * 10 + int(s[i])
            elif s[i] == '[':
                stack1.append(tmp)
                stack2.append(cur)
                cur = ""
                tmp = 0
            elif s[i] == ']':
                k = stack1.pop() if len(stack1) else 1
                decode = stack2.pop() if len(stack2) else ""
                decode += cur * k
                cur = decode
            else:
                cur += s[i]
            i += 1
        return cur