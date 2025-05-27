# 1. Don't forget to check the distance. Use vector properties.
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p = []
        p.append(p1)
        p.append(p2)
        p.append(p3)
        p.append(p4)
        
        p.sort(key = lambda x:(x[0], x[1]))
        
        v1 = (p[0][0] - p[1][0], p[0][1] - p[1][1])
        v2 = (p[2][0] - p[3][0], p[2][1] - p[3][1])
        v3 = (p[0][0] - p[2][0], p[0][1] - p[2][1])
        v4 = (p[1][0] - p[3][0], p[1][1] - p[3][1])
        
        def length(v):
            return v[0] * v[0] + v[1] * v[1]
        
        parallel = 0
        perpendicular = 0
        equal = 0
        if v1[0] * v2[1] == v1[1] * v2[0]:
            parallel += 1
            
        if v1[0] * v3[0] + v1[1] * v3[1] == 0:
            perpendicular += 1
            
        if v1[0] * v4[0] + v1[1] * v4[1] == 0:
            perpendicular += 1
            
        if length(v1) == length(v2) and length(v2) == length(v3) and length(v3) == length(v4):
            if length(v1) != 0 and length(v2)!= 0 and length(v3) != 0 and length(v4) != 0:
                equal += 1
   
        if perpendicular == 2 and parallel == 1 and equal == 1:
            return True
        return False
            
            
        
        
        
        