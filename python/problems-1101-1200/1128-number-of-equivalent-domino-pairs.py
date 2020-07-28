'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/w-20La0b2F4
'''

### solution 1 ###
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pair = {}
        count = 0
        for domino in dominoes:
            key = tuple(sorted(domino))
            count += pair.setdefault(key, 0)
            pair[key] += 1
        return count
