# First, what's worth noticing is the division between a positive and a negative numbers, we simply transfer it to normal division and add a negative sign.
# Second, about using power of two to speed up the division, that's worth learning.
# Third, overflow. It's an edge case.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        HALF_MIN_INT = MIN_INT // 2
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negatives = 0
        if dividend < 0:
            negatives += 1
            dividend = - dividend
        if divisor < 0:
            negatives += 1
            divisor = - divisor
        
        quotient = 0
        while dividend >= divisor:
            value = divisor
            tmp = 1
            while value * 2 <= dividend:
                value *= 2
                tmp *= 2
            quotient += tmp
            dividend -= value
        
        return -quotient if negatives == 1 else quotient