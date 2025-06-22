class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        mp = {}
        arr = []
        def is_prime(num):
            if num == 1:
                return False
            for k in range(2, int(sqrt(num) + 0.5) + 1):
                if num % k == 0 and num != k:
                    return False
            return True
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        for k, v in mp.items():
            arr.append(v)
        for vv in arr:
            if is_prime(vv):
                return True
        return False