'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH
https://youtu.be/xq_Y_uqpwPs
'''

### solution 1 ###
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
