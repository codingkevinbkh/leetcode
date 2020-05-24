'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        import math

        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

### solution 2 ###
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        import math

        def find_larger(found, target, sub_nums):
            for idx, num in enumerate(sub_nums):
                if num > target and (found == 2 or find_larger(found+1, num, sub_nums[idx+1:])):
                    return True
            return False
        
        return find_larger(0, -math.inf, nums)
