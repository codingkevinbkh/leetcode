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
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        dummy = Node()
        dummy.next = head
        curr = dummy
        junction = []
        while curr.next or curr.child or len(junction) > 0:
            if curr.child:
                junction.append(curr.next)
                curr.next = curr.child
                curr.child = None
                curr.next.prev = curr
                curr = curr.next
            elif curr.next:
                curr = curr.next
            else:
                curr_junc = junction.pop()
                if curr_junc:
                    curr.next = curr_junc
                    curr_junc.prev = curr
                    curr = curr.next
        return dummy.next
