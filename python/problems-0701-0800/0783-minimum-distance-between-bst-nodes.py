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
    def minDiffInBST(self, root: TreeNode) -> int:
        def find_min(head):
            value_max = []
            value_min = []
            diff = []
            if head.left:
                left_diff, left_max, left_min = find_min(head.left)
                if left_diff:
                    diff.append(left_diff)
                diff.append(abs(head.val-head.left.val))
                diff.append(abs(head.val-left_max))
                value_min.append(left_min)
            if head.right:
                right_diff, right_max, right_min = find_min(head.right)
                if right_diff:
                    diff.append(right_diff)
                diff.append(abs(head.val-head.right.val))
                diff.append(abs(head.val-right_min))
                value_max.append(right_max)
            
            if len(diff) == 0:
                return None, head.val, head.val
            else:
                value_max.append(head.val)
                value_min.append(head.val)
                return min(diff), max(value_max), min(value_min)
        ans, _, _ =  find_min(root)
        return ans
