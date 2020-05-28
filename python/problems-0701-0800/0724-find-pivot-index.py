'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        curr_sum = 0
        for i in range(len(nums)):
            if i > 0:
                curr_sum += nums[i-1]
            if curr_sum*2 == nums_sum-nums[i]:
                return i
        return -1
