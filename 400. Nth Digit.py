class Solution:
    def findNthDigit(self, n: int) -> int:
        nDig = 1 
        if n <= 9:
            return n
        numCount = 9  
        
        while n > nDig * numCount: 
            n -= nDig * numCount
            nDig += 1
            numCount *= 10
        ind = n % nDig - 1
        # recover the digit first (highest digit + how many nDigs), then position
        s = str(numCount // 9 + (n - 1) // nDig)[ind]
        return s