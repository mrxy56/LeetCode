class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l = len(palindrome)
        if l <= 1: # edge case
            return ""
        res = ""
        for i, ch in enumerate(palindrome):
            if ch!= 'a' and i != l // 2: # greedy but it cannot be the middle one or else palindrome
                if i != l - 1:
                    res = palindrome[:i] + 'a' + palindrome[i + 1:]
                else:
                    res = palindrome[:i] + 'a'
                return res
        res = palindrome[:l - 1] + 'b'
        return res