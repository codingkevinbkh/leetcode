'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH
https://youtu.be/JURjCajbJPU
'''

### solution 1 ###
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(candies)//2, len(set(candies)))
