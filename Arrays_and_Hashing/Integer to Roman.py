class Solution(object):
    def intToRoman(self, num):
        dict = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        sorted = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        roman_num = ""
        for number in sorted:
            roman_num += int(num/number)*dict[number]
            num -= number*int(num/number)
        return(roman_num) 
