class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for ch in chars:
            if not d.get(ch):
                d[ch] = 1
            else:
                d[ch] += 1
        
        def good(word):
            wd = {}
            for ch in word:
                if not wd.get(ch): # If you cannot get it, you need to create one.
                    wd[ch] = 1
                else:
                    wd[ch] += 1 # Else add one.
            for k, v in wd.items():
                if not d.get(k):
                    return 0
                if d[k] < v: # Use each character exactly once.
                    return 0
            return len(word)
        ans = 0
        for word in words:
            ans += good(word)
        return ans
            