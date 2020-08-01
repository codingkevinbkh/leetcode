'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/zqNewqfahcY
'''

### solution 1 ###
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        if len(A) != len(B):
            return False
        for _ in range(len(A)):
            if A == B:
                return True
            else:
                A = A[1:]+A[0]
        return False

### solution 2 ###
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        return B in A+A
