'''
歡迎訂閱我們的YouTube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有LeetCode實戰解題。
Check out our YouTube channel, we explain the solutions step by step with animation.
Please subscribe!

Coding Kevin BKH
https://youtu.be/h_VY1eokFBc
'''

### solution 1 ###
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1 != None:
            curr.next = l1
        if l2 != None:
            curr.next = l2
        return dummy.next

### solution 2 ###
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def findMin(n1, n2):
            if n1 == None:
                return n2
            if n2 == None:
                return n1
            if n1.val < n2.val:
                n1.next = findMin(n1.next, n2)
                return n1
            else:
                n2.next = findMin(n1, n2.next)
                return n2
        
        return findMin(l1, l2)
