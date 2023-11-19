# 1. To simplify the code, using two bools.
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        cnt = 0
        for i in range(l):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == l - 1) or (flowerbed[i + 1] == 0)
                if empty_left and empty_right:
                    cnt += 1
                    flowerbed[i] = 1
                    if cnt >= n:
                        return True
        return cnt >= n