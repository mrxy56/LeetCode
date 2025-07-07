# 1. Pay atttention to carry and leading zeros.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def multiply_one(num1, digit, zero):
            i = 0
            ans = []
            n1 = len(num1)
            carry = 0
            for j in range(zero):
                ans.append("0")
            while i < n1:
                x1 = int(num1[n1 - 1 - i])
                x = x1 * int(digit) + carry
                ans.append(str(x % 10))
                carry = x // 10
                i += 1
            while carry > 0:
                ans.append(str(carry % 10))
                carry = carry // 10
            return "".join(ans[::-1])
        def bigsum(num1, num2):
            n1 = len(num1)
            n2 = len(num2)
            ans = []
            i = 0
            carry = 0
            while i < n1 and i < n2:
                x1 = int(num1[n1 - 1 - i])
                x2 = int(num2[n2 - 1 - i])
                x = (x1 + x2 + carry) % 10
                ans.append(str(x))
                carry = (x1 + x2 + carry) // 10
                i += 1
            while i < n1:
                x1 = int(num1[n1 - 1 - i])
                x = (x1 + carry) % 10
                ans.append(str(x))
                carry = (x1 + carry) // 10
                i += 1
            while i < n2:
                x2 = int(num2[n2 - 1 - i])
                x = (x2 + carry) % 10
                ans.append(str(x))
                carry = (x2 + carry) // 10
                i += 1
            while carry > 0:
                ans.append(str(carry % 10))
                carry = carry // 10
            return "".join(ans[::-1])
        ls = []
        for i, num in enumerate(num2[::-1]):
            ls.append(multiply_one(num1, num, i))
        l = len(ls)
        tmp = ls[0]
        for i in range(1, l):
            tmp = deepcopy(bigsum(tmp, ls[i]))
        j = 0
        t = len(tmp)
        while j < t - 1 and tmp[j] == '0':
            j += 1
        return tmp[j:]