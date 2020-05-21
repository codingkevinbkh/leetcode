'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}  # key: diff, value: index
        for idx, num in enumerate(nums):
            if diff.get(num, None) == None:
                diff[target-num] = idx
            else:
                return [diff[num], idx]

### solution 2 ###
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = list(zip(nums, range(len(nums))))
        num_index.sort()
        left = 0
        right = len(num_index) - 1
        while left < right:
            curr_sum = num_index[left][0] + num_index[right][0]
            if curr_sum == target:
                return [num_index[left][1], num_index[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
