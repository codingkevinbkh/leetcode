'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        digits = int(math.log10(x))+1
        for i in range(digits//2):
            left_most = 10**(digits-2*i-1)
            left = x // left_most
            right = x % 10
            if right != left:
                return False
            x = (x - left*(left_most)) // 10
        return True

### solution 2 ###
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digit_map = {}
        pos = 0
        while x != 0:
            digit_map[pos] = x % 10
            pos += 1
            x //= 10
        for i in range(pos//2):
            if digit_map[i] != digit_map[pos-i-1]:
                return False
        return True
