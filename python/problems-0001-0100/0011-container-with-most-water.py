'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        visited = set()
        left, right = 0, len(height) - 1
        for h in sorted(height):
            if h not in visited:
                while height[left] < h:
                    left += 1
                while height[right] < h:
                    right -= 1
                if left != right:
                    max_water = max(max_water, (right-left)*h)
                visited.add(h)
        return max_water

### solution 2 ###
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_water = max(max_water, (min(height[left], height[right]) * (right-left)))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
