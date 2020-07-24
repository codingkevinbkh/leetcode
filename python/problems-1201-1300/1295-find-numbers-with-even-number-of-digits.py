'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/db7BLKRPA0A
'''

### solution 1 ###
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda x: int(log10(x)) % 2 == 1, nums)))

### solution 2 ###
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda x: len(str(x)) % 2 == 0, nums)))
