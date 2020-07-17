'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/xdpp9tH_sPQ
'''

### solution 1 ###
class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num > 0:
            if num == 1 or num % 2 == 0:
                count += 1
            else:
                count += 2
            num //= 2
        return count

### solution 2 ###
class Solution:
    def numberOfSteps (self, num: int) -> int:
        binary = bin(num)[2:]
        return len(binary)+binary.count('1')-1
