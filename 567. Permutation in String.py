# 1. Two pointers.
# 2. Identical string is also a permutation.
# 3. Remember to decrease the item pointed by i immediately. Note the edge case.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        i = -1
        j = -1
        mp1 = {}
        mp2 = {}
        for ch in s1:
            if ch in mp1:
                mp1[ch] += 1
            else:
                mp1[ch] = 1
        while j + 1 < m:
            j += 1
            if s2[j] in mp2:
                mp2[s2[j]] += 1
            else:
                mp2[s2[j]] = 1
            if j - i == n:
                if i >= 0:
                    mp2[s2[i]] -= 1
                flag = True
                for k, v in mp1.items():
                    if k not in mp2 or v != mp2[k]:
                        flag = False
                        break
                if flag:
                    return True
                i += 1

        return False
                