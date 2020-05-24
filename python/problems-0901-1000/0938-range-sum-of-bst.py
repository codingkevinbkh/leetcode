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
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def sum_node(head):
            current_sum = 0
            if head.left:
                current_sum += sum_node(head.left)
            if head.right:
                current_sum += sum_node(head.right)
            if head.val >= L and head.val <= R:
                current_sum += head.val
            return current_sum
        
        return sum_node(root)
