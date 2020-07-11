'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/UJMbLuOaeqg
'''

### solution 1 ###
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = 0
        for num in nums:
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num
        return (max1-1)*(max2-1)
