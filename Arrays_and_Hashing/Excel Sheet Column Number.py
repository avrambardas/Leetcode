class Solution(object):
    def titleToNumber(self, columnTitle):
        columnTitle = list(columnTitle)[::-1]
        letter_count = dict([(chr(i),i-64) for i in range(65,91)])

        number = letter_count[columnTitle[0]]
        mul = 26
        for letter in range(1, len(columnTitle)):
            number += letter_count[columnTitle[letter]]*mul
            mul *= 26

        return(number)
