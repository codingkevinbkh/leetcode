'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first = second = 0
        first_len, second_len = len(nums1), len(nums2)
        total_len = first_len + second_len
        values = []
        while len(values) < total_len//2+1:
            if first_len == first:
                values.append(nums2[second])
                second += 1
            elif second_len == second:
                values.append(nums1[first])
                first += 1
            else:
                if nums1[first] <= nums2[second]:
                    values.append(nums1[first])
                    first += 1
                else:
                    values.append(nums2[second])
                    second += 1
        if total_len % 2 == 0:
            return (values[-2]+values[-1])/2.0
        else:
            return values[-1]/1.0

### solution 2 ###
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(nums1) > len(nums2):
            a, b = nums2, nums1
        a_len, b_len = len(a), len(b)
        left, right = 0, a_len
        while left <= right:
            a_count = left + (right - left)//2 # number of element ofs left half
            b_count = (a_len + b_len)//2 - a_count # number of elements of left half
            a_max_left = -math.inf if a_count == 0 else a[a_count-1]
            a_min_right = math.inf if a_count == a_len else a[a_count]
            b_max_left = -math.inf if b_count == 0 else b[b_count-1]
            b_min_right = math.inf if b_count == b_len else b[b_count]
            
            if a_max_left <= b_min_right and b_max_left <= a_min_right:
                if (a_len + b_len) % 2 == 0:
                    return (max(a_max_left, b_max_left) + min(a_min_right, b_min_right))/2.0
                else:
                    return min(a_min_right, b_min_right)/1.0
            elif a_max_left > b_min_right:
                right = a_count-1
            else:
                left = a_count+1
