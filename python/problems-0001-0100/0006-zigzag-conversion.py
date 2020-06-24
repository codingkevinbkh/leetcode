'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/bxWrnTLStkg
'''

### solution 1 ###
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        strings = ['' for _ in range(numRows)]
        row, step = 0, 1
        for char in s:
            strings[row] += char
            if row == numRows-1:
                step = -1
            elif row == 0:
                step = 1
            row += step
        return ''.join(strings)
