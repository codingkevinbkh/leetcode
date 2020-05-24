'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_map = {}
        for num in arr:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1
        return len(num_map.values()) == len(set(num_map.values()))
