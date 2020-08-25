'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH
https://youtu.be/4FBWtr7XFfU
'''

### solution 1 ###
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda x: x**2, A))

### solution 2 ###
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A)-1
        ans = []
        while left <= right:
            if abs(A[left]) >= abs(A[right]):
                ans.append(A[left]**2)
                left += 1
            else:
                ans.append(A[right]**2)
                right -= 1
        return ans[::-1]
