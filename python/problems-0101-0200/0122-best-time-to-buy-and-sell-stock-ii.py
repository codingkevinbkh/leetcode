'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([p-p_prev for p_prev, p in zip(prices, prices[1:]) if p-p_prev > 0])
