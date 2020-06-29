'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import math

        min_price = math.inf
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p-min_price)
        return max_profit

### solution 2 ###
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        max_profit = 0
        for i in range(1, len(prices)):
            curr_profit = max(0, curr_profit+prices[i]-prices[i-1])
            max_profit = max(max_profit, curr_profit)
        return max_profit
