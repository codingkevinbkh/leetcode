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
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def sum_node(last_sum, head):
            curr_value = last_sum*2+head.val
            if head.left or head.right:
                total = 0
                if head.left:
                    total += sum_node(curr_value, head.left)
                if head.right:
                    total += sum_node(curr_value, head.right)
                return total
            else:
                return curr_value
            
        return sum_node(0, root)
