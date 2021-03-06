# Source: https://leetcode.com/problems/merge-two-sorted-lists/discuss/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# easy test case:
# [2,4,6,8]
# [1,3,5,7]

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        returnList = l3 = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        l3.next = l1 or l2
        return returnList.next
