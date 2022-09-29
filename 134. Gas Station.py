class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        cur = 0
        minnum = gas[0] - cost[0] # should not be 0
        mini = 0
        for i in range(l):
            cur += gas[i] - cost[i]
            if cur < minnum:
                minnum = min(minnum, cur)
                mini = i
        if cur >= 0:
            return (mini + 1) % l # Choose tho most costly trip, starting at any point before is less costly.
        else: # So make sure we gain enough fuels before getting into this costly trip.
            return -1