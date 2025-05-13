class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t.isdigit():
                s.append(t)
            elif len(t) == 1:
                x = int(s.pop())
                y = int(s.pop())
                if t == "+":
                    s.append(x + y)
                elif t == '-':
                    s.append(y - x)
                elif t == '*':
                    s.append(x * y)
                else:
                    s.append(y / x)
            else:
                s.append(int(t[1:]) * (-1))
        return int(s[0])
            