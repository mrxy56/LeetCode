class Solution:
    def intToRoman(self, num: int) -> str: # hard code, pay attention to 5 and 10
        thousand = ["", "M", "MM", "MMM"]
        hundred = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        one = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return thousand[num // 1000] + hundred[num % 1000 // 100] + ten[num % 100 // 10] + one[num % 10]
        