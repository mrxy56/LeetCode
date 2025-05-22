class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mp = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        new_num = []
        for ch in num[::-1]:
            if ch in mp:
                new_num.append(mp[ch])
            else:
                new_num.append("*")
        tmp = "".join(new_num)
        if tmp == num:
            return True
        else:
            return False