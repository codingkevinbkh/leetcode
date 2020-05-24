'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def intToRoman(self, num: int) -> str:
        num_to_letter = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        roman = ''
        power_of_ten = 1
        while num != 0:
            digit = num % 10
            current_roman = ''
            if digit == 9:
                current_roman = num_to_letter[9*power_of_ten]
            elif digit >= 5:
                current_roman = num_to_letter[5*power_of_ten]
                digit -= 5
            if digit == 4:
                current_roman = current_roman + num_to_letter[4*power_of_ten]
            elif digit < 4:
                current_roman = current_roman + num_to_letter[power_of_ten]*digit
            power_of_ten *= 10
            num //= 10
            roman = current_roman + roman
        return roman

### solution 2 ###
class Solution:
    def intToRoman(self, num: int) -> str:
        num_to_letter = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        roman = ''
        for digit in sorted(num_to_letter.keys(), reverse=True):
            while num >= digit:
                roman = roman + num_to_letter[digit]
                num -= digit
        return roman
