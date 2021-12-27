# Pretty tricky, but interesting counting sort.
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        self.store = collections.defaultdict(set)
        for log in logs:
            Id, time = log
            self.store[Id].add(time)
        ans = [0 for i in range(1, k + 1)]
        for Id, time in self.store.items():
            ans[len(self.store[Id]) - 1] += 1
        return ans