# https://leetcode.com/discuss/72582/concise-python-solution-with-comments
# http://www.acmerblog.com/leetcode-solution-insertion-sort-list-6242.html

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# import sys

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = dummy = ListNode(0)
        while head:
            if cur and cur.val > head.val: # reset pointer only when new number is smaller than pointer value
                cur = dummy
            while cur.next and cur.next.val < head.val: # classic insertion sort to find position
                cur = cur.next
            # cur.next, cur.next.next, head = head, cur.next, head.next # insert
            cur_next_tmp = cur.next
            head_next_tmp = head.next
            cur.next = head
            head.next = cur_next_tmp
            head = head_next_tmp
        return dummy.next