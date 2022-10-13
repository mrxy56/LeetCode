class Solution:
    def calculate(self, s: str) -> int:
        def cal(s):
            stack = []
            num = 0
            sign = '+'
            def cal_top():
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack[-1] *= num
                if sign == '/':
                    stack[-1] = int(stack[-1] / num)
                    
            while c := next(s):
                if c.isdigit():
                    num = int(c)
                elif c == '(':
                    num = cal(s)
                elif c in ')$':
                    cal_top()
                    ans = sum(stack)
                    return ans
                elif c in '+-*/':
                    cal_top()
                    sign = c
            
        ns = (s + '$').replace(' ', '')
        ls = filter(None, re.split(r'([+\-*/()\$])', ns))
        return cal(ls)