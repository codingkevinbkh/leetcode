'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s = re.sub('[' + string.punctuation + ' ]*', '' , s).lower()
        return s == s[::-1]

### solution 2 ###
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s = re.sub('[' + string.punctuation + ' ]*', '' , s).lower()
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
