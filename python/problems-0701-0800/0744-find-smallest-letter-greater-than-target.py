'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

### solution 2 ###
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target > letters[-1]:
            return letters[0]
        left, right = 0, len(letters)-1
        while left <= right:
            mid = left + (right-left)//2
            if letters[mid] > target and letters[mid-1] <= target:
                return letters[mid]
            elif letters[mid] > target and letters[mid-1] > target:
                right = mid-1
            else:
                left = mid+1
        return letters[0]
