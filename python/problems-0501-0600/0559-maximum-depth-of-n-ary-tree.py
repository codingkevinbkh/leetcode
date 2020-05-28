'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def traverse(head, prev_depth):
            curr_depth = prev_depth+1
            max_depth = curr_depth
            for child in head.children:
                max_depth = max(max_depth, traverse(child, curr_depth))
            return max_depth
        
        if root:
            return traverse(root, 0)
        return 0
