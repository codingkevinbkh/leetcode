'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/iAAZNizsqiM
'''

### solution 1 ###
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        schedule = []
        for t in trips:
            schedule.append([t[1], t[0]])
            schedule.append([t[2], -t[0]])
        schedule.sort()
        curr = 0
        for _, passenger in schedule:
            curr += passenger
            if curr > capacity:
                return False
        return True
