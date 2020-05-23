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
        digit_map = {}
        position = 0
        while pos_x != 0:
            digit_map[position] = pos_x % 10
            position += 1
            pos_x //= 10
        reverted_x, maximum = 0, 2147483647 # 2**31-1
        for i in range(position):
            reverted_x = reverted_x * 10 + digit_map[i]
            if reverted_x > maximum:
                return 0
        return reverted_x if x >= 0 else -reverted_x

### solution 2 ###
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
