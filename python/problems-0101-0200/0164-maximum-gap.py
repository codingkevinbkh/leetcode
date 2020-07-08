'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/qN0qvtFbCYw
'''

### solution 1 ###
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        if max_num == min_num:
            return 0
        interval = math.ceil((max_num-min_num)/(len(nums)-1))
        buckets = [[None, None] for _ in range((max_num-min_num)//interval+1)]
        for num in nums:
            bucket = buckets[(num-min_num)//interval]
            bucket[0] = min(bucket[0], num) if bucket[0] else num
            bucket[1] = max(bucket[1], num) if bucket[1] else num
        buckets = [b for b in buckets if b[0]]
        return max([buckets[i][0]-buckets[i-1][1] for i in range(1, len(buckets))])
