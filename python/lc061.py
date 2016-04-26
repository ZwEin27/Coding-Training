# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        size = 1
        tmp = head
        while tmp.next:
            tmp = tmp.next
            size += 1

        k = k%size

        left = head
        right = head

        for i in xrange(k):
            if right.next:
                right = right.next
            else:
                break

        while right.next:
            left = left.next
            right = right.next

        right.next = head
        head = left.next

        left.next = None
        return head
