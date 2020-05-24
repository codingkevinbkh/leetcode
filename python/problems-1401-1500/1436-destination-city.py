'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_city = set()
        to_city = set()
        for path in paths:
            from_city.add(path[0])
            to_city.add(path[1])
        return str(to_city.difference(from_city).pop())
