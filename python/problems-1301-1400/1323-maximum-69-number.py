'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def maximum69Number (self, num: int) -> int:
        import math
        
        digits = int(math.log10(num))+1
        curr_num = num
        curr_digit = 10**digits
        for i in range(digits):
            curr_digit //= 10
            if curr_num // curr_digit == 6:
                return num + 3*curr_digit
            curr_num %= curr_digit
        return num
