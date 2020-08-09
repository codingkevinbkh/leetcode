'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/ryykpSW-g4M
'''

### solution 1 ###
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        digit = {}
        for num in nums:
            count += digit.setdefault(num, 0)
            digit[num] += 1
        return count
