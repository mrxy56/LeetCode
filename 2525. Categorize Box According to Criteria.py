class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        def isBulky(length, width, height, mass):
            if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or length * width * height >= 10 ** 9:
                return True
            return False
        def isHeavy(length, width, height, mass):
            if mass >= 100:
                return True
            return False
        
        flag1 = isBulky(length, width, height, mass)
        flag2 = isHeavy(length, width, height, mass)
        
        if flag1 and flag2:
            return "Both"
        if not flag1 and not flag2:
            return "Neither"
        if flag1:
            return "Bulky"
        if flag2:
            return "Heavy"