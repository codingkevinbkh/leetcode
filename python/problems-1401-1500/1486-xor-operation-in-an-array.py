'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/QV5qfVcJUD0
'''

### solution 1 ###
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        for i in range(n):
            xor ^= start+i*2
        return xor

### solution 2 ###
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        last = start+2*(n-1)
        factor = 2
        if start % 4 < 2:
            start = 0
        else:
            n -= 1
        if n % 4 < 2:
            factor = 0
        if n % 2 == 0:
            last = 0
        return start ^ factor ^ last
