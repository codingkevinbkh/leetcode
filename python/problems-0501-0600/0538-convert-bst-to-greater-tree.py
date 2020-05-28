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
    def convertBST(self, root: TreeNode) -> TreeNode:
        def convert(head, parent_max):
            if head.right:
                head.val += convert(head.right, parent_max)
            else:
                head.val += parent_max
            if head.left:
                return convert(head.left, head.val)
            else:
                return head.val
        
        if root:
            convert(root, 0)
        return root
