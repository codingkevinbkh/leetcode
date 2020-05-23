'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def reverse(self, x: int) -> int:
        pos_x = abs(x)
        reverted_x, maximum = 0, 2147483647 # 2**31-1
        while pos_x != 0:
            reverted_x = reverted_x * 10 + pos_x % 10
            pos_x //= 10
            if reverted_x > maximum:
                return 0
        return reverted_x if x >= 0 else -reverted_x

### solution 2 ###
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        maximum = 2147483647 # 2**31-1
        reverted_x = int(str(abs(x))[::-1].strip("0"))
        if reverted_x > maximum:
            return 0
        return reverted_x if x >= 0 else -reverted_x
