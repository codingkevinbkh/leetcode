'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH
https://youtu.be/1gmuCPsD8a4
'''

### solution 1 ###
class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ''
        while n > 0:
            if len(ans) % 4 == 3:
                ans = '.' + ans
            ans = str(n % 10) + ans
            n //= 10
        return ans if ans else '0'

### solution 2 ###
class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ''
        n_str = str(n)
        for i in range(len(n_str)):
            if i > 0 and (len(n_str)-i) % 3 == 0:
                ans += '.'
            ans += n_str[i]
        return ans
