class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans1 = ans2 = 0
        l1 = len(arr1)
        l2 = len(arr2)
        base = 1
        for i in range(l1 - 1, -1, -1):
            ans1 += arr1[i] * base
            base *= -2
        base = 1
        for j in range(l2 - 1, -1, -1): 
            ans2 += arr2[j] * base
            base *= -2 # To my surprise, 2^1000 can be represented.
        ans1 += ans2
        stack = []
        if ans1 == 0: # Edge case
            return [0]
        while ans1:
            stack.append(ans1 & 1) # Trick is that you cannot % -2 directly, instead, use bit operation and change op.
            ans1 = -(ans1 >> 1)
        return reversed(stack)