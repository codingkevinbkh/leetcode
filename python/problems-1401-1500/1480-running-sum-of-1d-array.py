'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/wVztKtQ5z6A
'''

### solution 1 ###
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            running_sum.append(curr_sum)
        return running_sum
