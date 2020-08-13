'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/l1j01Z1AOAU
'''

### solution 1 ###
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        time = ceil(len(B)/len(A))
        for t in time, time+1:
            if B in A*t:
                return t
        return -1
