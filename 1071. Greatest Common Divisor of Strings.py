class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def divide(s, t):
            slen = len(s)
            tlen = len(t)
            if slen % tlen == 0:
                times = slen // tlen
                ns = ""
                for i in range(times):
                    ns = ns + t  
                if ns == s:
                    return True
            return False
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        l = len(str2)
        for i in range(l, 0, -1):
            tmp = str2[:i]
            if divide(str2, tmp) and divide(str1, tmp):
                return tmp
        return ""