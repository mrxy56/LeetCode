class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy: # instead of searching, we observe it and make full use of the rule.
            if tx == ty:
                break
            if tx > ty:
                if ty > sy:
                    tx %= ty # use module to save time
                else:
                    return (tx - sx) % ty == 0 
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
                
        return tx == sx and ty == sy # what if in the destination in the beginning?