'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        len_a = len(A)
        if len_a < 3:
            return False
        pos = neg = False
        for i in range(1, len_a):
            if not pos and not neg:
                if A[i]-A[i-1] > 0:
                    pos = True
                else:
                    return False
            elif pos and not neg:
                if A[i]-A[i-1] > 0:
                    pos = True
                elif A[i]-A[i-1] < 0:
                    neg = True
                else:
                    return False
            else:
                if A[i]-A[i-1] < 0:
                    neg = True
                else:
                    return False
        if pos and neg:
            return True
        else:
            return False

### solution 2 ###
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        len_a = len(A)
        if len_a < 3:
            return False
        left, right = 0, len_a-1
        while left < len_a-1 and A[left] < A[left+1]:
            left += 1
        while right > 0 and A[right] < A[right-1]:
            right -= 1
        if left == right and left != len_a-1 and right != 0:
            return True
        else:
            return False
