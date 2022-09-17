class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        cnt = 0
        for word in words:
            ans = ""
            for c in word:
                ans += mp[ord(c) - ord('a')]
            if ans not in s:
                s.add(ans)
                cnt += 1
        return cnt