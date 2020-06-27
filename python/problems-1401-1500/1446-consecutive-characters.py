'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/d5s_fkIEAPg
'''

### solution 1 ###
class Solution:
    def maxPower(self, s: str) -> int:
        prev_char = None
        count = 0
        power = 0
        for char in s:
            if char == prev_char:
                count += 1
            else:
                prev_char = char
                count = 1
            power = max(power, count)
        return power
