'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def convert(head):
            res = str(head.val)
            if head.left:
                res += '(' + convert(head.left) + ')'
            else:
                if head.right:
                    res += '()'
            if head.right:
                res += '(' + convert(head.right) + ')'
            return res
        
        if t:
            return convert(t)
        return ''
