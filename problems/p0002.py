# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers
# 1568 / 1568 test cases passed
# runtime: 64ms, beats 91.14% of python3 submissions
# memory usage: 14.3mb, beats 71.57% of python3 submissions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = l3 = ListNode(0)
        tmp = 0
        while l1 or l2 or tmp:
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            tmp, r = divmod(tmp, 10)
            l3.val = r
            if l1 or l2 or tmp:
                l3.next = ListNode(0)
                l3 = l3.next
        return start
