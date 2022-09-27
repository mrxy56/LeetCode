class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        ans = ""
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            ans += '-' # cannot div directly because there may be an scientific notation.
        numerator = abs(numerator)
        denominator = abs(denominator) # abs is important, or r is inaccurate.
        ans += str(numerator // denominator) + '.'
        ind = ans.index('.')
        if numerator % denominator == 0:
            return ans[:ind]
        r = numerator % denominator
        d = {}
        pos = ind + 1
        ans = ans[:pos]
        while r:
            if d.get(r):
                p = d.get(r)
                ans = ans[:p] + '(' + ans[p:] + ')'
                break
            else:
                d[r] = pos # we do not observe the actual repeat of the answer, but the internal remainder.
                r = r * 10
                ans = ans + str(r // denominator)
                r = r % denominator
            pos += 1
        return ans