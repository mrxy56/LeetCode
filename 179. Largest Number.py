# Define your own sort, lt means less than. pay attention to the starting with 0 situation.
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ls = []
        for num in nums:
            ls.append(str(num))
        new_nums = sorted(ls, key = LargerNumKey)
        ans = "".join(new_nums)
        return '0' if ans[0] == '0' else ans