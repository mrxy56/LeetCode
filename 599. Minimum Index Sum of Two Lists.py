class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp = {}
        ind_sum = 2000
        ans = []
        for i, word in enumerate(list1):
            if word not in mp:
                mp[word] = i
        for j, word in enumerate(list2):
            if word in mp:
                if j + mp[word] < ind_sum:
                    ind_sum = j + mp[word]
        for j, word in enumerate(list2):
            if word in mp and mp[word] + j == ind_sum:
                ans.append(word)
        return ans